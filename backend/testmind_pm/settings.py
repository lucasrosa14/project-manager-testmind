from pathlib import Path

# BASE_DIR aponta para a pasta raiz do projeto (onde está manage.py)
BASE_DIR = Path(__file__).resolve().parent.parent

ROOT_URLCONF = 'testmind_pm.urls'

SECRET_KEY = '+(14si4_fy_bu_&wu&9di2^ojliy-&urts=(na35h$_*igssj7'

# URL para arquivos estáticos (CSS, JS, imagens)
STATIC_URL = '/static/'

# Opcional: se quiser servir arquivos estáticos em pasta específica
STATICFILES_DIRS = [BASE_DIR / "static"]  # crie a pasta 'static' na raiz do backend

# Configuração de templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # agora funciona
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

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'users',
    'clients',
    'frameworks',
    'projects',
    'bugs',
    'corsheaders',
]

AUTH_USER_MODEL = 'users.User'

# Banco PostgreSQL (ajuste usuário/senha conforme seu docker)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'testmind_pm',
        'USER': 'testmind',
        'PASSWORD': 't3stm1nd',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',  # <-- adicione se não tiver
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # <-- deve estar depois da SessionMiddleware
    'django.contrib.messages.middleware.MessageMiddleware',     # <-- necessário
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

CORS_ALLOW_ALL_ORIGINS = True 

DEBUG = True

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
