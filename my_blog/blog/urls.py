from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('index/', views.IndexView.as_view(), name='index'),

    # 博客详情页
    path(r'article/<int:pk>/', views.ArticleView.as_view(), name='article'),
    # 归档页
    path('archives/', views.ArchivesView.as_view(), name='archives'),
    # 博客页
    path('articles/', views.ArticleListView.as_view(), name='articles'),
    # 搜索
    path('search/', views.SearchView.as_view(), name='search'),
    # 登陆
    path('login/', views.Login.as_view(), name='login'),
    # 注册
    path('register/', views.Register.as_view(), name='register'),
    # 激活
    path('activation/', views.Activation.as_view(), name='activation'),
    # 找回密码
    path('repasswd/', views.Repasswd.as_view(), name='repasswd')

    # # 邮箱登陆
    # path('login/email/', views.EmailLogin.as_view(), name='email_login'),
    # test base
    # path(r'base/', views.BaseView.as_view()),
]


# 全局404
handler404 = views.page_not_found
handler500 = views.page_error



