"""
Django settings for recruitment project.

Generated by 'django-admin startproject' using Django 3.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
# settings.py是整个Django项目的配置文件
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
ALLOWED_HOSTS = []


# Application definition
# INSTALLED_APPS它是Django项目里默认安装的应用
# 默认有安装django.admin、auth、sessions、messages和静态资源文件的应用，我们创建完了应用之后，也要往APPS的配置里面的结尾加上我们应用
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'jobs',
]
# MIDDLEWARE是启动的中间件，包括安全的中间件，防跨站攻击的中间件，跟认证授权的中间件
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'recruitment.urls'

# 这里指的是是默认使用了哪个模板引擎，模板引擎里也配置了有哪些上下文处理器，
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'recruitment.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases
# 这里指定了我们使用什么样的数据库，默认使用了本地的sqlite的数据库，这里我们可以配置数据库的路径，也可以替换数据库的引擎
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/
# 这里用来配置默认的语言，默认是英文的'en-us'，可以把它改成中文的'zh-hans'.
LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
# STATIC_URL = '/static/'是默认的别名，下面是新加的，两个需要配合使用
# 配好STATICFILES_DIRS形成的效果是找到static时进入的是下面定义的static文件夹下
STATICFILES_DIRS = [
    # BASE_DIR是路径，在上边有定义= Path(__file__).resolve().parent.parent，上一层的上一层的下面和static文件夹拼出来一个路径
    os.path.join(BASE_DIR,"static")# 配置一个静态文件夹，告诉Django去哪里拿
]

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
