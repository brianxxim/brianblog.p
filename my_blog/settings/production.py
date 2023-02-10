from .development import *


DEBUG = False

ALLOWED_HOSTS = ["127.0.0.1"]

MIDDLEWARE += [
    'django.middleware.csrf.CsrfViewMiddleware',
]

del STATICFILES_DIRS  # 静态文件交由nginx处理
STATIC_ROOT = os.path.join(RESOURCE_DIR, 'static')


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': '127.0.0.1',
        'PORT': 3306,
        'USER': 'root',
        'PASSWORD': '2E%bT#Y9Hg',
        'NAME': 'brian_blog',
    }
}

# 工程日志
LOGGING = {
    'version': 1,
    # 禁用现有记录器
    'disable_existing_loggers': True,
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