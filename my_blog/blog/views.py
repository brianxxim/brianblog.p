from logging import getLogger
import re
from datetime import datetime

from django.contrib.auth import login, authenticate, get_user_model
from django.contrib.auth.models import Group
from django.db import DatabaseError, transaction
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.cache import cache_page
from django.conf import settings
from django.core.cache import cache

from cache.alone import ArticleTag, TagInfo
from cache.paging import Pager
from _email import send_activation_email, send_repasswd_email
from whoosh_search.article import search
from . import constants
from .models.homes import Slideshow
from .models.articles import Recommend, Article, ArtArticleTag
from cache import statistics, alone
from encryption import verify_jwt

logger = getLogger('django')
User = get_user_model()


@method_decorator(cache_page(constants.CACHE_PAGE_TIME), name='get')
class IndexView(View):
    """
    获取首页
    """

    def get(self, request):
        # 获取轮播图
        pks = Slideshow.objects.values('slideshow_id').filter(is_delete=False).order_by("?")[
              :constants.SLIDESHOW_SHOW_COUNT]
        slideshows = alone.SlideshowInfo.mget([pk['slideshow_id'] for pk in pks])

        # 推荐文章
        pks = Recommend.objects.values('recommend_id').filter(is_delete=False).order_by('?')[
              :constants.RECOMMEND_ARTICLE_SHOW_COUNT]
        art_recommends = alone.ArticleInfo.mget_by_relation(pks=[i['recommend_id'] for i in pks])

        # 热门文章
        pks = statistics.ArticleReadCount.get_top(constants.HOT_ARTICLE_SHOW_COUNT)
        articles_hot = alone.ArticleInfo.mget_by_relation(pks=pks)

        return render(request, 'index.html', {
            'slideshows': slideshows,
            'art_recommends': art_recommends,
            'articles_hot': articles_hot
        })


@method_decorator(cache_page(constants.CACHE_SEARCH_PAGE_TIME), name='get')
class SearchView(View):
    """
    搜索视图
    """

    def get(self, request):
        text = request.GET.get('text')
        page_num = request.GET.get('page_num', '1')
        # request.path if re.match('^/search.*', request.path) else '/'
        total_page = 0
        articles = []

        if not text:
            # 无关键字
            return redirect('/')

        pks = search(text, pagenum=page_num)

        if pks:
            total_page = constants.SEARCH_MAX_PAGE
            articles = alone.ArticleInfo.mget_by_relation(pks)

        return render(request, 'search.html', {
            'page_num': page_num,
            'total_page': total_page,
            'articles': articles,
            'text': text
        })


@method_decorator(cache_page(constants.CACHE_PAGE_TIME), name='get')
class ArticleView(View):
    """
    文章详情视图
    """

    def get(self, request, pk):
        article = alone.ArticleInfo().get_by_relation(pk)

        if not article:
            # 文章不存在
            return render(request, '404.html', {'message': '文章不存在或已被删除!'})

        article['content'] = alone.ArticleDetail().get(pk)
        pks = ArticleTag().get(pk)
        article['tags'] = TagInfo().mget(pks)

        # 浏览加1
        statistics.ArticleReadCount.incr(pk)

        return render(request, 'detail.html', {
            'article': article
        })


@method_decorator(cache_page(constants.CACHE_DETAIL_PAGE_TIME), name='get')
class ArchivesView(View):
    """
    文章归档视图
    """

    def get(self, request):
        pk_times = statistics.ArticleCreateTime.get_top(constants.ARCHIVE_SHOW_COUNT, score=True)
        pks = [pt['pk'] for pt in pk_times]

        articles = alone.ArticleInfo().mget(pks=pks)
        for index in range(len(articles)):
            articles[index]['create_time'] = datetime.fromtimestamp(int(pk_times[index]['score']))

        return render(request, 'archive.html', {
            'articles': articles
        })


@method_decorator(cache_page(constants.CACHE_PAGE_TIME), name='get')
class ArticleListView(View):
    """
    博客列表视图
    过滤条件：category、tag、paging(分页)、全部展示
    """

    def get(self, request):
        """
        :param request:
        :return: 总数据长度，总页数，当前页数，当前页数据
        """
        cid = request.GET.get('category_id', '')
        tid = request.GET.get('tag_id', '')
        current_page = request.GET.get('page_num', '')
        category = None
        tag = None

        # 是否分页
        if not re.match(r'^\d+$', str(current_page)):
            # 没有分页或分页有误
            current_page = 1

        if re.match(r'^\d+$', str(cid)):
            # 根据分类获取博文
            pk_queryset = Article.objects.values('article_id').filter(category_id=cid, is_delete=False).order_by(
                '-create_time')
            category = alone.CategoryInfo().get(cid)

            page_key = 'cid:{}'.format(cid)

        elif re.match(r'^\d+$', str(tid)):
            # 获取指定标签博文
            pk_queryset = ArtArticleTag.objects.values('article_id').filter(tag_id=tid)
            tag = alone.TagInfo().get(tid)

            page_key = 'tid:{}'.format(tid)

        else:
            # 获取所有博文
            pk_queryset = Article.objects.values('article_id').filter(is_delete=False).order_by('-create_time')
            page_key = 'all'

        # 缓存保存分页器的同时, 保存数据总长度。统一在存在缓存时不查询数据库
        pager = Pager(page_key, pk_queryset)

        pks = pager.page(current_page).object_list
        articles = alone.ArticleInfo().mget_by_relation(pks)

        return render(request, 'articles.html', {
            'total_count': pager.total_count,  # 数据总长度
            'total_page': pager.num_pages,  # 总页数
            'articles': articles,  # 每页数据
            'current_page': current_page,  # 当前页
            'tag': tag,
            'category': category,
        })


@method_decorator(cache_page(5), name='get')
class Login(View):
    """
    登陆视图
    """

    def get(self, request):
        _next = request.GET.get('next')
        return render(request, 'login.html', {'next': _next})

    def post(self, request):
        """
        登陆业务
        :param request:
        :return:
        """
        username = request.POST.get('username')
        password = request.POST.get('password')
        next = request.GET.get('next')

        if username is None:
            return JsonResponse({'message': '请输入用户名'})
        if password is None:
            return JsonResponse({'message': '请输入密码'})

        if not re.match(r'^/', next):
            next = '/admin'

        user = authenticate(username=username, password=password)
        if user:
            if user.is_staff or user.is_superuser:
                login(request, user)
                return JsonResponse({'url': next})

        return JsonResponse({'message': "用户名或密码错误！"}, status=403)


@method_decorator(cache_page(5), name='get')  # 缓存不可用, csrf需要刷新
class Register(View):
    """
    注册视图
    """
    CACHE_KEY = 'register:{}'  # key: ip value:次数

    @staticmethod
    def response(message, status=403, **kwargs):
        """
        返回格式
        {'message': message, ....}
        """
        result = {'message': message}
        result.update(kwargs)

        resp = JsonResponse(result)
        resp.status_code = status

        return resp

    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')  # 判断是否使用代理
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]  # 使用代理获取真实的ip
        else:
            ip = request.META.get('REMOTE_ADDR')  # 未使用代理获取IP

        if username is None:
            return self.response('请输入用户名!', 400)
        if email is None:
            return self.response('请输入邮箱', 400)
        if password is None:
            return self.response('请输入密码', 400)
        if password2 is None:
            return self.response('请输入二次密码', 400)
        if password != password2:
            return self.response('二次密码不一致!')

        if not re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email):
            return self.response('邮箱格式错误!')

        register_number = cache.get(self.CACHE_KEY.format(ip)) or 0
        if register_number > constants.REGISTER_NUMBER_LIMIT:
            return self.response('请勿频繁注册!')

        try:
            if User.objects.filter(username=username, is_staff=True).count():
                return self.response('用户名已存在!', 422)

            if User.objects.filter(email=email, is_staff=True).count():
                return self.response('邮箱已存在!', 422)

        except DatabaseError as e:
            logger.error(e)
            return self.response('注册失败!', 500)

        with transaction.atomic():
            sid = transaction.savepoint()

            try:
                # 创建用户
                user = User.objects.filter(username=username, email=email).first()
                if user is None:
                    user = User.objects.create_user(username=username, email=email)
                user.set_password(password)

                g = Group.objects.get(name=constants.ORDINARY_USER_GROUP_NAME)
                g.user_set.add(user)
                g.save()

                # 发送邮件
                if not send_activation_email(user, ip=ip):
                    raise Exception('发送邮件失败!')

                transaction.savepoint_commit(sid)  # 提交事务
            except Exception as e:
                logger.error(e)
                transaction.savepoint_rollback(sid)  # 回滚事务
                return self.response('注册失败!', 500)

        cache.set(self.CACHE_KEY.format(ip), register_number + 1, constants.REGISTER_EXCEED_WAIT_TIME)

        # login(request, user)
        return self.response('注册成功! 请前往邮箱激活账号.', 200, url='/login', show_msg='注册成功! 请前往邮箱激活账号.')


class Activation(View):
    """
    激活用户
    """
    CACHE_KEY = 'activation:token:{}'

    def get(self, request):
        token = request.GET.get('token')
        resp = render(request, 'login.html', {'show_msg': '激活链接已失效!'}, status=403)

        if not token:
            return resp

        if cache.get(self.CACHE_KEY.format(token)):
            return resp

        payload = verify_jwt(token)
        if not payload:
            return resp

        # token只能使用一次
        cache.set(self.CACHE_KEY.format(token), True, timeout=settings.USER_ACTIVATION_EXPIRE_SECONDS)

        pk = payload.get('id')
        email = payload.get('email')
        if not User.objects.filter(id=pk, email=email, is_staff=False).update(is_staff=True):
            return resp

        return render(request, 'login.html', {'show_msg': '注册成功!', 'message': '欢迎回来!'})


class Repasswd(View):
    """找回密码"""
    CACHE_KEY = 'respasswd:token:{}'

    def post(self, request):
        """发送找回密码链接"""
        email = request.POST.get('email')
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')  # 判断是否使用代理
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]  # 使用代理获取真实的ip
        else:
            ip = request.META.get('REMOTE_ADDR')  # 未使用代理获取IP

        # 1 验证参数
        if email is None:
            return JsonResponse({'message': '请输入邮箱'})
        if not re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email):
            return JsonResponse({'message': '请检查邮箱格式'}, status=400)

        user = User.objects.filter(email=email, is_staff=True).first()

        if user is None:
            return JsonResponse({'message': '请检查邮箱格式'}, status=400)

        # 2 发送邮箱
        if not send_repasswd_email(user, ip):
            return JsonResponse({'message': '发送邮箱失败!'}, status=500)

        return JsonResponse({'message': '发送成功, 请你检查您邮箱!'}, status=200)

    def get(self, request):
        """验证找回密码token"""
        token = request.GET.get('token')
        resp = render(request, 'login.html', {'show_msg': '链接已失效!'}, status=403)
        if not token:
            return resp

        if cache.get(self.CACHE_KEY.format(token)):
            return resp

        payload = verify_jwt(token)
        if not payload:
            return resp

        # token只能使用一次
        cache.set(self.CACHE_KEY.format(token), True, timeout=settings.USER_REPASSWD_EXPIRE_SECONDS)

        user = User.objects.filter(id=payload.get('id'), email=payload.get('email')).first()
        if user is None:
            return resp

        login(request, user)
        return redirect('/admin/')


# 全局404
@cache_page(60 * 60)
def page_not_found(request, exception):
    return render(request, '404.html', status=404)


@cache_page(60 * 60)
def page_error(request):
    return render(request, '404.html', {
        'message': '页面错误!!'
    }, status=500)


class EmailLogin(View):
    """
    邮件登陆
    """
    pass
