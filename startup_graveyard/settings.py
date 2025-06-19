# from pathlib import Path
# import os


# BASE_DIR = Path(__file__).resolve().parent.parent
# SECRET_KEY = 'django-insecure-demo-key'
# DEBUG = True
# ALLOWED_HOSTS = []

# INSTALLED_APPS = [
#     'django.contrib.admin',
#     'django.contrib.auth',
#     'django.contrib.contenttypes',
#     'django.contrib.sessions',
#     'django.contrib.messages',
#     'django.contrib.staticfiles',
#     'accounts',
#     'widget_tweaks',
#     'startups',
# ]

# MEDIA_URL = '/media/'
# MEDIA_ROOT = BASE_DIR / 'media'


# MIDDLEWARE = [
#     'django.middleware.security.SecurityMiddleware',
#     'django.contrib.sessions.middleware.SessionMiddleware',
#     'django.middleware.common.CommonMiddleware',
#     'django.middleware.csrf.CsrfViewMiddleware',
#     'django.contrib.auth.middleware.AuthenticationMiddleware',
#     'django.contrib.messages.middleware.MessageMiddleware',
#     'django.middleware.clickjacking.XFrameOptionsMiddleware',
# ]

# ROOT_URLCONF = 'startup_graveyard.urls'

# TEMPLATES = [
#     {
#         'BACKEND': 'django.template.backends.django.DjangoTemplates',
#         'DIRS': [os.path.join(BASE_DIR, 'accounts', 'templates')],
#         'APP_DIRS': True,
#         'OPTIONS': {
#             'context_processors': [
#                 'django.template.context_processors.debug',
#                 'django.template.context_processors.request',
#                 'django.contrib.auth.context_processors.auth',
#                 'django.contrib.messages.context_processors.messages',
#                 'accounts.context_processors.recent_startups',
#             ],
#         },
#     },
# ]

# WSGI_APPLICATION = 'startup_graveyard.wsgi.application'

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'startup_graveyard',
#         'USER': 'graveyard_user',
#         'PASSWORD': 'graveyard123',
#         'HOST': 'localhost',
#         'PORT': '5432',
#     }
# }

# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, 'static'),
# ]

# AUTH_PASSWORD_VALIDATORS = []

# LANGUAGE_CODE = 'en-us'
# TIME_ZONE = 'UTC'
# USE_I18N = True
# USE_TZ = True

# STATIC_URL = '/static/'

# DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# LOGIN_URL = 'login'
# LOGIN_REDIRECT_URL = 'dashboard'
# LOGOUT_REDIRECT_URL = 'login'

from pathlib import Path
import os
import dj_database_url

# --- Base Settings ---
BASE_DIR = Path(__file__).resolve().parent.parent

# --- Secret Key ---
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'django-insecure-demo-key')

# --- Debug ---
DEBUG = os.environ.get('DEBUG', 'False') == 'True'

# --- Hosts ---
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '127.0.0.1').split(',')

# --- Installed Apps ---
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'accounts',
    'widget_tweaks',
    'startups',
]

# --- Media ---
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# --- Static ---
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

# --- Whitenoise for static file serving ---
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# --- Middleware ---
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Whitenoise added here
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# --- URLConf ---
ROOT_URLCONF = 'startup_graveyard.urls'

# --- Templates ---
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'accounts', 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'accounts.context_processors.recent_startups',
            ],
        },
    },
]

# --- WSGI ---
WSGI_APPLICATION = 'startup_graveyard.wsgi.application'

# --- Database ---
DATABASES = {
    'default': dj_database_url.config(
        default='postgresql://graveyard_user:graveyard123@localhost:5432/startup_graveyard',
        conn_max_age=600
    )
}

# --- Auth Redirects ---
LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'dashboard'
LOGOUT_REDIRECT_URL = 'login'

# --- Password Validators (Disable for demo purposes) ---
AUTH_PASSWORD_VALIDATORS = []

# --- Localization ---
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# --- Auto Field ---
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
