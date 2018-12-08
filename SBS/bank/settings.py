"""
Django settings for bank project.

Generated by 'django-admin startproject' using Django 2.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
import datetime

from django.contrib import messages
from dotenv import load_dotenv

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

load_dotenv()


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv("DEBUG", False)

ALLOWED_HOSTS = ['*']
if not DEBUG:
    ALLOWED_HOSTS = ['192.168.2.235']

# Application definition

INSTALLED_APPS = [
    'django_su',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'axes',  # django-axes
    'app',
    'session_security',
    'django_otp',
    'django_otp.plugins.otp_totp',
    'qrcode',
    'guardian',
    'django_filters',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django_otp.middleware.OTPMiddleware',
    'session_security.middleware.SessionSecurityMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'app.middleware.ActiveUserMiddleware',
]

ROOT_URLCONF = 'bank.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'app/templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django_su.context_processors.is_su',
            ],
        },
    },
]

WSGI_APPLICATION = 'bank.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases
DB_PASS = os.getenv("DB_PASS")
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'sbs',
        'USER': 'admin',
        'PASSWORD': DB_PASS,
        'HOST': 'localhost',
        'PORT': '',
        'ATOMIC_REQUESTS': True,
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 10,
        }
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
    {
        'NAME': 'app.validators.MyPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
STATIC_URL = '/static/'

# User Model
AUTH_USER_MODEL = 'app.MyUser'

# Mail Settings
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'love.sbs2018@gmail.com'
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_PASS")
EMAIL_PORT = 587


# Misc Settings
APPEND_SLASH = True

LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/dashboard/'
LOGOUT_REDIRECT_URL = '/'
OTP_LOGIN_URL = '/login/'

SESSION_EXPIRE_AT_BROWSER_CLOSE = True
CSRF_USE_SESSIONS = True

MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'
MESSAGE_TAGS = {
    messages.ERROR: 'danger',
}


# Session-Security
SESSION_SECURITY_WARN_AFTER = 5400
SESSION_SECURITY_EXPIRE_AFTER = 6000


# Django-Su
SU_LOGIN_REDIRECT_URL = '/dashboard/'
SU_LOGOUT_REDIRECT_URL = '/'
SU_LOGIN_CALLBACK = 'app.su_login.su_login_by_admin'
SU_CUSTOM_LOGIN_ACTION = 'app.su_login.login_action'


# Django-Guardian
ANONYMOUS_USER_NAME = None


AUTHENTICATION_BACKENDS = [
    'axes.backends.AxesModelBackend',
    'django.contrib.auth.backends.ModelBackend',
    'django_su.backends.SuBackend',
    'guardian.backends.ObjectPermissionBackend',
]

# TODO Test Dummy cache in Live

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    },
    'axes_cache': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}

# Axes Settings
AXES_CACHE = 'axes_cache'
AXES_FAILURE_LIMIT = 5
AXES_USE_USER_AGENT = True
AXES_COOLOFF_TIME = datetime.timedelta(minutes=1)
AXES_ONLY_USER_FAILURES = False
AXES_NEVER_LOCKOUT_WHITELIST = False
AXES_IP_WHITELIST = False

# Admins
ADMINS = [('Meet', 'meet16055@iiitd.ac.in')]

# Logger
SYSTEM_LOG_PATH = os.path.join(BASE_DIR, 'app/log/System/logs.log')
TRANSACTION_LOG_PATH = os.path.join(BASE_DIR, 'app/log/Transactions/SecureTransactionLogs.log')
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': "[%(asctime)s] %(levelname)s %(message)s",
            'datefmt': "%d/%b/%Y %H:%M:%S"
        },
    },
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': SYSTEM_LOG_PATH,
            'formatter': 'standard',
            'when': 'midnight',
            'interval': 1,
        },
        'transactionfile': {
            'level': 'INFO',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': TRANSACTION_LOG_PATH,
            'formatter': 'standard',
            'when': 'midnight',
            'interval': 1,
        },
    },
    'loggers': {
        'app': {
            'handlers': ['file'],
            'level': 'INFO',
            'propagate': True,
        },
        'app.views.transactions': {
            'handlers': ['transactionfile'],
            'level': 'INFO',
            'propagate': True,
        },
    },
}

# Production Settings
if not DEBUG:
    CSRF_COOKIE_SECURE = True
    SESSION_COOKIE_SECURE = True

    SECURE_CONTENT_TYPE_NOSNIFF = True
    SECURE_BROWSER_XSS_FILTER = True
    SECURE_SSL_REDIRECT = True
    X_FRAME_OPTIONS = 'DENY'

    # Django-Axes Settings
    AXES_COOLOFF_TIME = datetime.timedelta(minutes=10)

    # Session-Security Settings
    SESSION_SECURITY_WARN_AFTER = 240
    SESSION_SECURITY_EXPIRE_AFTER = 300
