
import os.path
from pathlib import Path


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-l$1-7(0nk*ge72fonp69+cm$-g0o+4x9^3fa+55^s_uu(@-kgk'

# SECURITY WARNING: don't run with debug turned on in production!
# 默认DEBUG是True的，在测试的环境下面可以看到DEBUG出错的各种信息，包括异常的信息，在生产环境中应该把DEBUG设置成false
# 不然别人访问应用的时候都能够区看到各种调试信息
DEBUG = True

# ALLOWED_HOSTS 里面配置有哪些IP地址可以访问，默认是只有127.0.0.1的端口可以访问，可以再这里输入服务器外网的IP到外边访问
# 通常不会在这里配，而是用一个网关服务，比如是用Nginx用Tengine来做这个网关，把Django的应用开放出去
ALLOWED_HOSTS = ["localhost","127.0.0.1","*",]

# LOGIN_REDIRECT_URL = '/' # 投简历的用户登录成功了之后的，默认跳转的url，这个默认跳转的是首页
# SIMPLE_BACKEND_REDIRECT_URL = '/accounts/login/'# 投简历的用户在后端注册成功了之后登录的url

# INSTALLED_APPS它是Django项目里默认安装的应用
# 默认有安装django.admin、auth、sessions、messages和静态资源文件的应用，我们创建完了应用之后，也要往APPS的配置里面的结尾加上我们应用
INSTALLED_APPS = [
    'grappelli',
    'bootstrap4',
    # 'registration',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app01',
    'debug_toolbar',
    # 富文本编辑器
    'ckeditor',
    'ckeditor_uploader',
    # 系统模块
    'system',
    # 景点模块
    'sight',
    # 用户账户
    'accounts',
    # 订单模块
    'order',
    'master.apps.MasterConfig',

]
# MIDDLEWARE是启动的中间件，包括安全的中间件，防跨站攻击的中间件，跟认证授权的中间件
MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    # 'interview.performance.performance_logger_middleware',# 自定义的中间件
    'django.middleware.security.SecurityMiddleware',# 常用的安全拦截处理
    'django.contrib.sessions.middleware.SessionMiddleware',# 处理用户的登录信息
    'django.middleware.locale.LocaleMiddleware',# 多语言中间件
    'django.middleware.common.CommonMiddleware',#
    # 'django.middleware.csrf.CsrfViewMiddleware',# 处理跨站攻击
    'django.contrib.auth.middleware.AuthenticationMiddleware',# 处理用户认证登录
    'django.contrib.messages.middleware.MessageMiddleware',# 处理用户操作的提示消息
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'app01.middleware.MyMiddleware',# 自定义的中间件
]

ROOT_URLCONF = 'recruitment.urls'

# 这里指的是是默认使用了哪个模板引擎，模板引擎里也配置了有哪些上下文处理器，
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',# django.template.backends.jinja2.Jinja2，它用jinjia2文件夹
        'DIRS': [os.path.join(BASE_DIR,'templates')],# html文件夹的位置和名称，用这种方式关联可以解决跨平台的路径问题
        'APP_DIRS': True,# 决定模板引擎是否应该进入每个已安装的应用中查找模板
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
    # {
    #     'BACKEND': 'django.template.backends.jinja2.Jinja2',
    #     'DIRS': [os.path.join(BASE_DIR,'jinja2')],
    # },
]

WSGI_APPLICATION = 'recruitment.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases
# 这里指定了我们使用什么样的数据库，默认使用了本地的sqlite的数据库，这里我们可以配置数据库的路径，也可以替换数据库的引擎
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'orm',# 要链接的数据库，连接前需要创建好
        'USER': 'root',# 要连接数据库的用户名
        'PASSWORD': '123456',# 要连接数据库的密码
        'HOST': '127.0.0.1',# 连接的主机
        'PORT': 3306,
    }
}


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

from django.utils.translation import gettext_lazy as _
# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/
# 这里用来配置默认的语言，默认是英文的'en-us'，可以把它改成中文的'zh-hans'.
LANGUAGES = [
    ('zh-hans', _('Chinese')),
    ('en', _('English')),
]

LANGUAGE_CODE = 'zh-Hans'

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)

TIME_ZONE = 'Asia/Shanghai' # 可以设置时区 'Asia/Shanghai' 'UTC'

USE_I18N = True
USE_L10N = True

USE_TZ = False # False是使用系统当前时间


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
# STATIC_URL = '/static/'是默认的别名，下面是新加的，两个需要配合使用
# 配好STATICFILES_DIRS形成的效果是找到static时进入的是下面定义的static文件夹下
STATICFILES_DIRS = [
    # BASE_DIR是路径，在上边有定义= Path(__file__).resolve().parent.parent，上一层的上一层的下面和static文件夹拼出来一个路径
    os.path.join(BASE_DIR,"static")# 配置一个静态文件夹，告诉Django去哪里拿
]

MEDIA_URL = '/media/' # 上传静态文件用到
MEDIA_ROOT = os.path.join(BASE_DIR,'medias')


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

'''下面语句的作用是，在处理表的时候，打印出对数据库的处理过程和日志记录
# 一共四个组件handlers日志的处理器，记录到哪里；loggers定义了哪一些日志的记录器，、filters过滤器，定义一系列的处理链；
# formatters记录日志配置的格式，记录了什么内容
'''
# LOGGING= {
#     'version': 1,
#     'disalbe_existing_loggers':False, # 是否禁用现在已有的其他的logger
#     'handlers':{
#         'console':{
#             'level':'DEBUG',
#             'class':'logging.StreamHandler',
#         },
#     },
#     'loggers':{
#         'django.db.backends':{ # django_python3_ldap
#             'handlers':['console'],
#             'propagate':True,
#             'level':'DEBUG',
#         },
#     }
# }

# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'formatters': {
#         'simple': {# 当前时间(年月日时分秒)、是哪个类、是多少行、日志级别、消息
#             'format': '%(asctime)s %(name)-12s %(lineno)d %(levelname)-8s %(message)s',
#         },
#     },
#     'handlers': {
#         'console': {# 往控制台输出
#             'class': 'logging.StreamHandler',
#             'formatter': 'simple',
#         },
#
#         'mail_admins': {# 发送到邮件处理器
#             'level': 'ERROR',
#             'class': 'django.utils.log.AdminEmailHandler',
#         },
#         'file': {# 记录到指定文件
#             #'level': 'INFO',
#             'class': 'logging.FileHandler',
#             'formatter': 'simple',
#             'filename': os.path.join(os.path.dirname(BASE_DIR), 'recruitment.admin.log'),
#         },
#
#         'performance': {
#             # 'level': 'INFO',
#             'class': 'logging.FileHandler',
#             'formatter': 'simple',
#             'filename': os.path.join(os.path.dirname(BASE_DIR), 'recruitment.performance.log'),
#         },
#     },
#
#     'root': {# root是一个系统全局级别默认的日志记录器，是logger里特殊的，这里定义了往控制台和文件同时输出
#         'handlers': ['console','file'],
#         'level': 'INFO',# INFO跟以上级别.包括ERROR、WARNING、CRITICAL都会记下来
#     },
#
#     'loggers': {
#         "django_python3_ldap": {# 这个生效要先安装ldap
#             "handlers": ["console", "file"],
#             "level": "DEBUG",
#         },
#
#         "interview.performance": {
#             "handlers": ["console", "performance"],
#             "level": "INFO",
#             "propagate": False,
#         },
#     },
# }

DINGTALK_WEB_HOOK = ""
INTERNAL_IPS = [
    '127.0.0.1'
]


# 富文本编辑器文件上传的位置
CKEDITOR_UPLOAD_PATH = "uploads/"

MEDIA_URL = 'http://localhost:8080/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'medias')

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}
# 指定自定义的用户模型，用来替换Django的默认模型，在accounts里也写了一个User类
AUTH_USER_MODEL = 'accounts.User'
# 对应accounts.views里的user_info方法，用以测试跳转使用
LOGIN_URL = '/accounts/user/login/'