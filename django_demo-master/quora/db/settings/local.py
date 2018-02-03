

SECRET_KEY = 'm$s5(9n3qnx9*9=n29bc_kld6n*gp*=_t(*3^n$+bk9i*a9ez$'

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'quora.db.quora',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)


DATABASES = {
'default': {
    'ENGINE': 'django.db.backends.mysql',
    'NAME': 'Quora',
    'USER': 'root',
    'PASSWORD': 'akshay123',
    'HOST': 'localhost',
    'PORT': '',
},
}



