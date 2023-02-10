from django.contrib import admin
from django import forms
from django.contrib.auth.forms import UserChangeForm as UserChangeFormBase, UserCreationForm as UserCreationFormBase
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.db.models.base import ModelBase

from .models import articles, homes, users
# Register your models here.


class UserFormBase(forms.Form):
    is_delete = forms.BooleanField(label='逻辑删除', required=False, help_text='指明用户是否可用。')
    is_staff = forms.BooleanField(label='工作人员', required=False, help_text='指明用户是否可以登录到这个管理站点。')
    email = forms.CharField(label='电子邮件地址', max_length=254)


class UserCreationForm(UserCreationFormBase, UserFormBase):
    pass


class UserChangeForm(UserFormBase, UserChangeFormBase):
    pass


class AdminBase(admin.ModelAdmin):
    """
    后台管理定制基类
    # 列表是可变数据类型, self.ordering == cls.ordering
    # 对象A: 在__init__中添加给self.ordering添加属性, 也就是给cls.ordering添加属性
    # 对象B: 在__init__中获取self.ordering, 得到了对象A设置的cls.ordering
    # 解决?
    # 方案1: 在每个Base子类中设置cls.ordering=[], 保证每次初始化对象时cls.ordering是空的
    # 方案2: 将cls.ordering类型定义为 tuple ()
    # 方案3: 使用copy模块拷贝


    # 不可变类型, 当值发生改变, 需要新的内存地址. 表示不是同一对象.
    # 可变类型, 当值发生改变, 内存地址不变, 表示是同一对象.
    # 不可变数据类型
    a = 100
    b = a
    id(a) == id(b)  # True
                    # b = a = 100 为了节省内存, 内存地址是一样的
    a += 1
    id(a) == id(b)  # False
                    # a=101, b=100  因为数据不可改变,a的改变需要申请新的内存地址,而b使用原来的内存地址

    # 可变数据类型
    a = [100]
    b = a
    id(a) == id(b)  # True

    a.append(100)
    id(a) == id(b) # True
            # a = b =[100, 100] 可变数据类型, 引用相同的内存地址




    浅拷贝：copy.copy()
    1. 不可变类型的浅拷贝：只拷贝了对象的内存地址（即使嵌套了可变类型）
    a =([100, 200], 'a')
    b = copy.copy(a)
    id(a)  # 139777647586504
    id(b)  # 139777647586504
    id(a[0])  # 139777647219784
    id(b[0])  # 139777647219784

    2. 可变类型的浅拷贝：拷贝对象. 但如果存在不可变类型, 依然只拷贝地址
    a =[(100, 200), 'a']
    b = copy.copy(a)
    id(a) # 139777647130760
    id(b) # 139777647586184
    id(a[0]) # 139777647219784
    id(b[0]) 139777647219784

    深拷贝：copy.deepcopy()
    1.不可变对象的深拷贝：
        ((100, 200), 'a')  # 如果最外层和子层全部是不可变类型, 拷贝最外层和子层对象的内存地址
        id(a)  # 140595617708360
        id(b)  # 140595617708360
        id(a[0])  # 140595617281416
        id(b[0])  # 140595617281416

        ([100, 200], 'a')  # 当嵌套了可变类型, 拷贝了最外层和子层对象
        id(a)  # 139796155334216
        id(b)  # 139796154864328
        id(a[0])  # 139796164749896
        id(b[0])  # 139796155026504


    2. 可变类型的深拷贝：
        # 不管是可变嵌套不可变, 还是不可变嵌套可变.
        # 对于可变类型, 不管是外层还是子层. 拷贝的都是对象
        # 对于不可变类型, 拷贝的总是内存引用

        [[100, 200], 'a']  # 拷贝所有对象, 生成新内存地址
        In [16]: id(a)
        Out[16]: 139796154418824

        In [17]: id(b)
        Out[17]: 139796051311752

        In [18]: id(a[0])
        Out[18]: 139796154417992

        In [19]: id(b[0])
        Out[19]: 139796051311240

        [(100, 200), 'a']  # 当嵌套了不可变对象, 拷贝外层对象, 拷贝子层对象的引用
        In [22]: id(a)
        Out[22]: 139796051168520

        In [23]: id(b)
        Out[23]: 139796051330952

        In [24]: id(b[0])
        Out[24]: 139796063578888

        In [25]: id(a[0])
        Out[25]: 139796063578888

    总结:
    不可变类型拷贝的是引用
    可变类型拷贝的是对象

    浅拷贝: 倾向于拷贝引用
    对于不可变类型: 拷贝引用
    对于可变类型: 拷贝对象. 但嵌套了不可变类型, 依然只拷贝引用

    深拷贝: 倾向于拷贝对象
        对于不可变类型, 拷贝引用. 但是嵌套了可变类型, 它就(相当于)转型成了可变类型, 于是拷贝里里外外所有对象
        对于可变类型, 拷贝对象. 但嵌套了不可变类型, 依然只拷贝引用

    应用场景:
        1. 希望通过拷贝解决上面类似的内存冲突问题.
        对于可变类型拷贝对象, 在__init__使用cls.ordering时, 生成新的内存. 修改时便不会影响到cls.ordering, 下个对象使用cls.ordering时, cls.ordering是干净的.
        对于不可变类型拷贝引用, 不可变类型本身在改变值后生成新内存.
        综合考虑可以使用copy.copy()
        2. 对象需要更换内存地址时 object = copy.copy(object)
        3.


    字符串是不可变数据类型
    数字是不可变数据类型
    元组是不可变数据类型() tuple()

    列表是可变数据类型 []
    字典是可变数据类型 {}
    集合是可变数据类型 {:}
    """
    model: object = None
    list_display = []
    list_display_links = []
    list_editable = []
    list_per_page = 10
    ordering = []

    save_as = True

    def __new__(cls, *args, **kwargs):
        """
        初始化管理类
        :param args:
        :param kwargs:
        """
        # 如果子类设置list_display的属性为tuple，复制后仍然是tuple, 而django要求list
        # cls.list_display = copy(cls.list_display)
        # cls.list_display_links = copy(cls.list_display_links)
        # cls.list_editable = copy(cls.list_editable)
        # cls.ordering = copy(cls.ordering)

        cls.list_display = list(cls.list_display)
        cls.list_display_links = list(cls.list_display_links)
        cls.list_editable = list(cls.list_editable)
        cls.ordering = list(cls.ordering)

        if not isinstance(cls.model, ModelBase):
            raise TypeError('model error', cls.model)

        primary_id = cls.model.__name__.lower() + '_id'
        if not hasattr(cls.model, primary_id):
            primary_id = 'id'

        # 可进入编辑的字段
        cls.list_display.insert(0, primary_id)
        cls.list_display_links.insert(0, primary_id)

        if not cls.ordering:
            cls.ordering.append(primary_id)

        if hasattr(cls.model, 'create_time'):
            if 'create_time' not in cls.list_display:
                cls.list_display.append('create_time')

        if hasattr(cls.model, 'update_time'):
            if 'update_time' not in cls.list_display:
                cls.list_display.append('update_time')

        if hasattr(cls.model, 'is_delete'):
            if 'is_delete' not in cls.list_display:
                cls.list_display.append('is_delete')
                cls.list_editable.append('is_delete')

        return object.__new__(cls)

    #
    # def __init__(self, model, admin_site,):
    #     if not isinstance(self.model, ModelBase):
    #         raise TypeError('model error', self.model)
    #     # self.list_display = list(self.list_display)
    #     # self.list_display_links = list(self.list_display_links)
    #     # self.list_editable = list(self.list_editable)
    #     # self.ordering = list(self.ordering)
    #     self.list_display = copy(self.list_display)
    #     self.list_display_links = copy(self.list_display_links)
    #     self.list_editable = copy(self.list_editable)
    #     self.ordering = copy(self.ordering)
    #
    #     primary_id = self.model.__name__.lower() + '_id'
    #     # 可进入编辑的字段
    #     self.list_display.insert(0, primary_id)
    #     self.list_display_links.insert(0, primary_id)
    #
    #     self.ordering.insert(0, primary_id)
    #
    #     if hasattr(self.model, 'create_time'):
    #         if 'create_time' not in self.list_display:
    #             self.list_display.append('create_time')
    #
    #     if hasattr(self.model, 'update_time'):
    #         if 'update_time' not in self.list_display:
    #             self.list_display.append('update_time')
    #
    #     if hasattr(self.model, 'is_delete'):
    #         if 'is_delete' not in self.list_display:
    #             self.list_display.append('is_delete')
    #             self.list_editable.append('is_delete')
    #     super().__init__(model, admin_site,)
    #


class CategoryAdmin(AdminBase):
    """
    文章分类后台管理定制
    """
    model = articles.Category
    list_display = ['name']
    list_display_links = ['name']
    search_fields = ['name']


class TagAdmin(AdminBase):
    """
    标签后台管理定制
    """
    model = articles.Tag
    list_display = ['name']
    list_display_links = ['name']
    search_fields = ['name']


class RecommendAdmin(AdminBase):
    """
    推荐后台管理定制
    """
    model = articles.Recommend
    list_display = ['article']
    list_display_links = ['article']
    search_fields = ['article']


class ArticleAdmin(AdminBase):
    """
    文章后台管理定制
    """
    model = articles.Article
    # list_display = ['title', 'cover', 'category', 'author']
    # list_display_links = ['title']
    # search_fields = ['title', 'content']
    # list_editable = ['category', 'author']

    list_display = ['title', 'cover', 'read_count', 'comment_count', 'category', 'author', 'is_delete']
    list_display_links = ['title']
    search_fields = ['title', 'digest', 'content']
    list_editable = ['category']
    ordering = ['-update_time']

    add_fieldsets = (
        (None, {'fields': ('title', 'cover', 'category', 'tag', 'digest', 'content')}),
        ('控制', {'fields': ('read_count', 'comment_count', 'author', 'is_delete')}),
    )

    fieldsets = add_fieldsets

    def get_queryset(self, request):
        """
        控制显示的查询查询集
        :param request:
        :return:
        """
        user = request.user

        queryset = self.model.objects.all()

        if not user.is_superuser:
            # 非超级用户返回自己的数据
            queryset = queryset.filter(author_id=user.pk)

        ###### 以下为父类源代码 ######
        ordering = self.get_ordering(request)
        if ordering:
            queryset = queryset.order_by(*ordering)
        return queryset

    def get_list_display(self, request):
        """
        控制显示的字段
        :param request:
        :return:
        """
        if not request.user.is_superuser:
            return self.list_display[:5]

        return self.list_display

    def get_fieldsets(self, request, obj=None):
        """
        控制可编辑字段
        :param request:
        :param obj:
        :return:
        """
        if not request.user.is_superuser:
            return self.fieldsets[:1]

        return self.fieldsets

    def save_model(self, request, obj, form, change):
        """
        控制用户修改其它用户数据 and 保存文章时设置作者
        :param request:
        :param obj:
        :param form:
        :param change:
        :return:
        """
        user = request.user
        # 限制保存权限
        if user.is_superuser or user.id == obj.pk:
            # 设置作者
            obj.author = request.user
            obj.save()


class LinkAdmin(AdminBase):
    """
    链接后台管理定制
    """
    model = homes.Link
    list_display = ['name', 'title']
    list_display_links = ['name']
    search_fields = ['name', 'title']
    # list_editable = ['title']


class SlideshowAdmin(AdminBase):
    """
    轮播图后台管理定制
    """
    model = homes.Slideshow
    list_display = ['title', 'image']
    list_display_links = ['title']
    search_fields = ['title']


class NoticeAdmin(AdminBase):
    """
    滚动消息后台管理定制
    """
    model = homes.Notice
    list_display = ['content']
    list_display_links = ['content']
    search_fields = ['content']


class UserAdmin(AdminBase, BaseUserAdmin):
    """
    用户后台管理定制
    """
    model = users.User
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('username', 'email', 'phone', 'is_staff', 'is_active')
    list_display_links = list_display[:2]

    list_editable = ('is_staff', 'is_active',)

    fieldsets = (
        ('基本信息', {'fields': ('username', 'email', 'phone', 'password')}),
        ('权限', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        ('重要日期', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'phone', 'password1', 'password2'),
        }),
    )

    # current_user_fieldsets = fieldsets[:1]
    # current_user_list_display = list_display[:2]

    def get_queryset(self, request):
        """
        控制显示的查询集
        :param request:
        :return:
        """
        user = request.user

        queryset = self.model.objects.all()

        if not user.is_superuser:
            # 非超级用户返回自己的数据
            queryset = queryset.filter(id=user.pk)

        ###### 以下为父类源代码 ######
        ordering = self.get_ordering(request)
        if ordering:
            queryset = queryset.order_by(*ordering)
        return queryset

    def get_list_display(self, request):
        """
        控制显示的字段
        :param request:
        :return:
        """
        if not request.user.is_superuser:
            return self.list_display[:3]

        return self.list_display

    def get_fieldsets(self, request, obj=None):
        """
        控制可编辑字段
        :param request:
        :param obj:
        :return:
        """
        if not request.user.is_superuser:
            return self.fieldsets[:1]

        return self.fieldsets

    def save_model(self, request, obj, form, change):
        """
        控制用户修改其它用户数据
        """
        user = request.user

        if user.is_superuser or user.id == obj.pk:
            obj.save()


registers = (CategoryAdmin, TagAdmin, RecommendAdmin,
             ArticleAdmin, LinkAdmin, SlideshowAdmin, NoticeAdmin, UserAdmin)
for Admin in registers:
    admin.site.register(Admin.model, Admin)

# admin.site.register(articles.Tag, TagAdmin)
# admin.site.register(articles.Recommend, RecommendAdmin)
# admin.site.register(articles.Article, ArticleAdmin)
# admin.site.register(homes.Link, LinkAdmin)
# admin.site.register(homes.Slideshow, SlideshowAdmin)
# admin.site.register(homes.Notice, NoticeAdmin)
# admin.site.register(users.User, BaseUserAdmin)

admin.site.site_header = 'BrianAdmin'
admin.site.site_title = 'BrianAdmin'
# admin.site.index_title = '大江狗管理后台'
