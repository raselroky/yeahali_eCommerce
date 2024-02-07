
from pathlib import Path
import os


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-#iusz8-a#64^+lvfl64wj#0*#(u((#uzo7pvcso9d*!zf6nppa'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'payments.apps.PaymentsConfig',
    'rest_framework',
    'corsheaders',
    'rest_framework.authtoken',
    #'rest_framework_simplejwt',
    'phonenumber_field',
    'django_countries',
    'paypal.standard.ipn',
    'user_management',
    'categories',
    'products',
    'contact_us',
    'dashboard',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    
]

ROOT_URLCONF = 'yeahali.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR,"templates"],
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

WSGI_APPLICATION = 'yeahali.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators


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
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES':(
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES':(
        #'rest_framework.permissions.IsAuthenticated',
    )
}

# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'
STATIC_ROOT=os.path.join(BASE_DIR, "static")
#STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]

MEDIA_URL = 'media/' 
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


CORS_ALLOWED_ORIGINS = [
    'http://127.0.0.1:8000',
    'http://localhost:8000',
    'http://localhost:8080',
    'http://localhost:3000',
    'https://raselroky.pythonanywhere.com',
]
CORS_ALLOW_ALL_ORIGINS = True 
CORS_ALLOW_CREDENTIALS = True

CORS_ORIGIN_WHITELIST = (
    'https://raselroky.pythonanywhere.com',
    'http://localhost:3000',  # for localhost (REACT Default)
    'http://192.168.10.45:3000', # for network
)
CSRF_TRUSTED_ORIGINS = [
    'https://raselroky.pythonanywhere.com',
    'http://localhost:3000',  # for localhost (REACT Default)
    'http://192.168.0.50:3000',  # for network 
    'http://localhost:8080',  # for localhost (Developlemt)
    'http://192.168.0.50:8080',  # for network (Development)
]
CORS_ALLOW_METHODS = ['DELETE','GET','OPTIONS','PATCH','POST','PUT',]
CORS_ALLOW_HEADERS = ['accept','accept-encoding','authorization','content-type','dnt','origin','user-agent','x-csrftoken','x-requested-with',]


#paypal 
PAYPAL_RECIEVER_EMAIL='sb-tmz5g29237875@business.example.com'
PAYPAL_TEST=True

#stripe
STRIPE_SECRET_KEY=''
STRIPE_PUBLISHABLE_KEY='pk_test_51NyDoVBPyua4ViM3knSMNTwrFdpN9xCkCqOOZsXXqcPvOLzKzNknpI5YGA7DR8W2hx7WfBRFleUyUkFe0dda1h72001QY4fJiO'

#AUTH_USER_MODEL="authentication.Users"