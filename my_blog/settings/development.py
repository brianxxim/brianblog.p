import os
import sys


class BossConfig(object):
    """
    博主信息
    """
    EMAIL = 'chengrip@foxmail.com'  # 本站邮箱
    WEB_NAME = 'BrianBlog'  # 本站名称
    DOMAIN_NAME = 'brianblog.asia'  # 本站域名
    WEB_LINK = 'https://{}/'.format(DOMAIN_NAME)  # 本站链接
    ABOUT_ME_LINK = 'https://itcheng.brianblog.asia/'  # 关于我链接
    GITHUB_LINK = 'https://github.com/brianxxim'  # github链接
    BLOG_SOURCE_CODE = GITHUB_LINK + 'brianblog'


BOSS = BossConfig()

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(BASE_DIR, 'my_blog'))
sys.path.insert(0, os.path.join(os.path.join(BASE_DIR, 'my_blog'), 'common'))

RESOURCE_DIR = os.path.join(os.path.join(BASE_DIR, 'my_blog'), 'resources')

SECRET_KEY = 'i0i45S1A57ReOyVUo168QpFhr6JOd@kaTceXIzaisUtV6q9@7F'

DEBUG = True

ALLOWED_HOSTS = ["*"]

# csrf允许通过哪些地址请求
CSRF_TRUSTED_ORIGINS = [".{}".format(BOSS.DOMAIN_NAME)]
#  匹配原理: host: 请求域名, pattern: CSRF_TRUSTED_ORIGINS
#  return (
#         pattern[0] == '.' and (host.endswith(pattern) or host == pattern[1:]) or
#         pattern == host
#     )


INSTALLED_APPS = [
    # 'jet.dashboard',  # jet仪表盘
    # 'jet',
    'simpleui',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 富文本编辑器
    'ckeditor',
    'ckeditor_uploader',
    # 搜索(已废弃)
    # 'haystack',
    'blog.apps.BlogConfig',
    # ssl插件 废弃 使用gunicorn代理
    # 'sslserver',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'middlewares.CensusMiddlewares',
]

ROOT_URLCONF = 'my_blog.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(RESOURCE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'common.context_processors.global_variable',  # base全局上下文
            ],
        },
    },
]

WSGI_APPLICATION = 'my_blog.wsgi.application'

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# 数据库
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': 'mysqlbrianblog.mysql.database.azure.com_3306',
        'PORT': 3306,
        'USER': 'root',
        'PASSWORD': '7obUPLnJMt',
        'NAME': 'brian_blog',
    }
}

# 缓存
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'unique-snowflake',
    },
    'cache': {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/0",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    },
    'caches': {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/0",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    },
    'news': {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    },
    'session': {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

# session缓存位置
SESSION_ENGINE = "django.contrib.sessions.backends.cache"  # 表示使用本地缓存
SESSION_CACHE_ALIAS = "session"


# 静态资源
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(RESOURCE_DIR, 'static')]
# 收集static时使用
# STATIC_ROOT = os.path.join(RESOURCE_DIR, 'static')

# 默认主键的类型
DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

# 用户类
AUTH_USER_MODEL = 'blog.User'

# 认证系统
AUTHENTICATION_BACKENDS = ['common.auth.UsernameMobileModelBackend']

# 七牛文件系统
DEFAULT_FILE_STORAGE = 'common.file_storage.FileStorage'
# QINIU_BASE_URL = 'http://ri8q77bs7.hn-bkt.clouddn.com/'
QINIU_BASE_URL = 'https://image.brianblog.asia/'
QINIU_ACCESS_KEY = 'Nm1Ww5KDQ9erqZx4Wk-N2NqzvQmP-rOPQqzKAbgO38'
QINIU_SECRET_KEY = 'QsxFzt7yhFjF-wthibIoRoEfQnU5acpxGgmfwk'
QINIU_BUCKET_NAME = 'brianblog2'
# 上传凭证过期时间 (s)
QINIU_TOKEN_EXISTS = 10 * 60

# 邮箱
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# SMTP服务器配置
EMAIL_HOST = 'smtp.sina.com'
EMAIL_PORT = 25
# SMTP认证配置
EMAIL_HOST_USER = 'brianblogblogger@sina.com'
EMAIL_HOST_PASSWORD = '9d88b25af6e8d1b1'
# 发件人抬头; 格式 签名<xxx@xx.com> or xxx@xx.com
DEFAULT_FROM_EMAIL = 'BrianBlog<brianblogblogger@sina.com>'
SERVER_EMAIL = DEFAULT_FROM_EMAIL

# error日志邮箱
ADMINS = (
    ('BRIAN', BOSS.EMAIL),
)
# 非空链接，却发生404错误，发送通知MANAGERS
SEND_BROKEN_LINK_EMAILS = True
MANAGERS = ADMINS

# 新闻API
NEWS_API = 'https://api.jisuapi.com/news/get'
NEWS_APPKEYS = ["5604123bc2fb930", "4391b24c9d6d81136"]

# 畅言云评
JY_APPID = 'cywaAMztL'
JY_SECRET_KEY = 'e382497c2eb9a468ee7f932a58c99600'

# SimpleUI后台
# LOGO
SIMPLEUI_LOGO = '/static/logo.png'

# 离线模式
SIMPLEUI_STATIC_OFFLINE = True

# 隐藏SimpleUI广告
SIMPLEUI_HOME_INFO = False
# 隐藏使用分析
SIMPLEUI_ANALYSIS = False
# 自定义图标 参考: https://fontawesome.com/
SIMPLEUI_ICON = {
    '推荐文章': 'fab fa-apple',
}
# 自定义菜单
SIMPLEUI_CONFIG = {
    # 保留原有菜单
    'system_keep': True,
    # 动态菜单
    'dynamic': False,
    # 菜单
    'menus': [
        {
            'name': 'About Blogger',
            'icon': 'el-icon-user',
            'url': BOSS.ABOUT_ME_LINK,
            'newTab': True  # 在新标签页中打开
        }
    ]
}

# 工程日志
LOGGING = {
    'version': 1,
    # 禁用现有记录器
    'disable_existing_loggers': False,
    # 过滤器
    "filters": {
        # DEBUG 为 False 时，该过滤器才会传递记录
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
        # DEBUG 为 True 时，该过滤器才会传递记录
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    # 格式化工具
    'formatters': {
        'verbose': {
            'format': '%(levelname)s: [%(asctime)s]  '
                      '%(pathname)s, line %(lineno)d, in %(funcName)s \n  "%(message)s"'
        },
    },
    # 处理器
    'handlers': {
        # 控制台
        'console': {
            'level': 'INFO',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
        # 文件
        'file': {
            'level': 'INFO',
            'filters': ['require_debug_false'],
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(os.path.join(BASE_DIR, 'logs'), 'blog_info.log'),
            'maxBytes': 300 * 1024 * 1024,
            'backupCount': 3,
            'formatter': 'verbose'
        },

        # 可疑操作
        'waring': {
            'level': 'WARNING',
            'filters': ['require_debug_false'],
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(os.path.join(BASE_DIR, 'logs'), 'blog_waring.log'),
            'maxBytes': 100 * 1024 * 1024,  # 文件大小
            'backupCount': 3,  # 文件数量
            'formatter': 'verbose'
        },

        # 邮件提醒
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },

    # 日志器
    'loggers': {
        'django': {
            # 注册使用哪些日志处理器
            'handlers': ['console', 'file', 'waring', 'mail_admins'],
            'propagate': True,
            # 日志传递级别 DEBUG > INFO > WARNING > ERROR > CRITICA
            'level': 'INFO',
        },
    }
}


# ckeditor
# 文件上传目录; 此配置会被common.file_storage.py覆盖
# CKEDITOR_UPLOAD_PATH = 'uploads/'
# 资源位置
CKEDITOR_UPLOAD_PATH = os.path.join(os.path.join(RESOURCE_DIR, 'static'), 'ckeditor')
# 编辑器样式
CKEDITOR_CONFIGS = {
    'digest': {
        'toolbar': (
            # ['div','Source','-','Save','NewPage','Preview','-','Templates'],
            ['Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord'],
            # ['Undo','Redo','-','Find','Replace','-','SelectAll','RemoveFormat'],
            # ['Form','Checkbox','Radio','TextField','Textarea','Select','Button', 'ImageButton','HiddenField'],
            ['Bold', 'Italic', 'Underline', 'Strike', '-', 'Subscript', 'Superscript'],
            ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', 'Blockquote'],
            ['JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock'],
            # ['Link','Unlink','Anchor'],
            ['Image', 'Flash', 'Table', 'HorizontalRule', 'Smiley', 'SpecialChar', 'PageBreak'],
            ['Styles', 'Format', 'Font', 'FontSize'],
            ['TextColor', 'BGColor'],
            # ['Maximize','ShowBlocks','-','About', 'pbckcode'],
            ['Blockquote', 'CodeSnippet'],
        ),
        'height': 100,
        'width': 1200,
        'tabSpaces': 4,
        'extraPlugins': 'autogrow',  # 代码插件
    },
    'default': {
        'skin': 'moono',
        # 'skin': 'office2013',
        'height': 400,
        'width': 1200,
        'autoGrow_maxHeight': 600,
        'toolbar_MyConfig': [
            # 第一排
            {'name': '辅助', 'items': ['Undo', 'Redo', '-',
                                     'SelectAll', 'Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord', '-',
                                     'Save', 'Templates', 'Source', 'Maximize', 'ShowBlocks', ]}, '/',
            # 第二排
            # {'name': 'HTML表单', 'items': ['Form', 'Checkbox', 'Radio', 'TextField', 'Textarea', 'Select', 'Button', 'ImageButton', 'HiddenField']}, '/',
            {'name': '字体',
             'items': ['Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript', 'TextColor', 'BGColor',
                       ]},
            {'name': '段落', 'items': ['Outdent', 'Indent', '-',
                                     'BidiLtr', 'BidiRtl', 'Language']},
            {'name': '样式', 'items': [
                'Blockquote', 'CreateDiv', '-',
                'NumberedList', 'BulletedList', '-',

            ]},
            # {'name': '链接', 'items': ['Link', 'Unlink', 'Anchor']},
            {'name': '插入',
             'items': ['Image', 'Flash', 'Table', 'HorizontalRule', 'Smiley', 'SpecialChar', 'PageBreak', 'Iframe']},
            '/',
            # 第三排
            {'name': 'styles', 'items': ['Styles', 'Format', 'Font', 'FontSize']},
            {'name': 'colors', 'items': ['-',
                                         'Find', 'Replace', 'RemoveFormat', 'CodeSnippet', 'Markdown']},
        ],
        'toolbar': 'MyConfig',
        # 可折叠工具栏
        'toolbarCanCollapse': True,
        # 不知道具体作用的javascript显示引擎
        'mathJaxLib': '//cdn.mathjax.org/mathjax/2.2-latest/MathJax.js?config=TeX-AMS_HTML',
        'tabSpaces': 4,
        'extraPlugins': ','.join([
            'uploadimage',  # 图片上传
            'codesnippet',  # 代码显示
            'markdown',
            'div',
            'autolink',
            'autoembed',
            'embedsemantic',
            'autogrow',
            # 'devtools',
            'widget',
            'lineutils',
            'clipboard',
            'dialog',
            'dialogui',
            'elementspath',
        ]),
        # 'extraPlugins': ','.join(['autogrow', 'codesnippet']),  # 代码插件
        # 'external_plugin_resources': [(
        #      'prism',
        #      '/static/prism/',
        #      'prism.js'
        #  ),],
    }
}


# 后台默认风格
# # layui风格
# SIMPLEUI_DEFAULT_THEME = 'layui.css'
# # 紫色风格
# SIMPLEUI_DEFAULT_THEME = 'purple.css'
# # Admin Lte风格
# SIMPLEUI_DEFAULT_THEME = 'admin.lte.css'
# # Element-ui风格
# SIMPLEUI_DEFAULT_THEME = 'element.css'


# Elasticsearch(已废弃)
# HAYSTACK_CONNECTIONS = {
#     'default': {
#         'ENGINE': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',
#         'URL': 'http://106.14.6.185:9200/',
#         'INDEX_NAME': 'brian_blog',  # es索引库的名称
#     },
# }
# 当添加、修改、删除数据时，自动更新索引
# HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'

# 已废弃@ 文件保存改用七牛云
# MEDIA_URL = '/media/'  # 上传图片的路径
# MEDIA_ROOT = os.path.join(BASE_DIR, '/media/')  # 上传图片的根路径

# 用户注册激活过期时间
USER_ACTIVATION_EXPIRE_SECONDS = 60 * 60 * 24
# 用户找回密码过期时间
USER_REPASSWD_EXPIRE_SECONDS = 60 * 30
