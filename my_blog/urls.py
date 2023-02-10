from django.contrib import admin
from django.urls import path, include
from my_blog.blog.views import Login


urlpatterns = [
    # 本地访问文件路径
    # re_path('^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    # haystack搜索
    # re_path(r'^search/', include('haystack.urls')),

    # ckeditor文件上传
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('admin/login/', Login.as_view(), name='login'),
    path('admin/', admin.site.urls, name='admin'),
    path('', include('my_blog.blog.urls'))
]

