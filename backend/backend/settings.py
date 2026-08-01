from pathlib import Path
import os  #lire les variables d'environnement de system 
from dotenv import load_dotenv 


BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / '.env')  # charge le fichier .env pour que os.getenv() puisse lire dedans
SECRET_KEY = os.getenv('SECRET_KEY')
DEBUG = True #mode développement, affiche les erreurs détaillées. En production on met False
INSTALLED_APPS =[
    'django.contrib.admin', # interface admin Django
    'django.contrib.auth',  # système login/logout
    'django.contrib.contenttypes',
    'django.contrib.sessions',# gestion des sessions
    'django.contrib.messages',# messages flash (succès, erreur...)
    'django.contrib.staticfiles', # fichiers CSS/images statiques
    'rest_framework', # pour créer ton API REST ← on a ajouté ça
    'corsheaders',  # pour autoriser React à parler à Django ← on a ajouté ça
    'products'
]

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''imagine que chaque requête HTTP (quand React demande quelque chose à Django) doit passer par une série de portes de sécurité avant d'arriver au code.'''

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware', #t'as le droit de rentrer ?
    'django.middleware.security.SecurityMiddleware',#la connexion est sécurisée ?
    'django.contrib.sessions.middleware.SessionMiddleware',  #tu es connecté ?
    'django.middleware.common.CommonMiddleware', # corrections techniques 
    'django.middleware.csrf.CsrfViewMiddleware',   #c'est bien toi qui envoies ça 
    'django.contrib.auth.middleware.AuthenticationMiddleware', # qui es-tu exactement ?
    'django.contrib.messages.middleware.MessageMiddleware',  #prépare les messages 
    'django.middleware.clickjacking.XFrameOptionsMiddleware' #protège contre certaines attaques
]
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------
ROOT_URLCONF = 'backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


#------------------------------------------------------------------------------------------------------------------------------------
'''database settings :'''
DATABASES = {
    'default':{
        'ENGINE':'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME'),
        'USER':os.getenv('DB_USER'),
        'PASSWORD':os.getenv('DB_PASSWORD'),
        'HOST':os.getenv('DB_HOST'),
        'PORT':os.getenv('DB_PORT')
    }
}


AUTH_PASSWORD_VALIDATORS = [
    {'NAME':'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME':'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME':'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME':'django.contrib.auth.password_validation.NumericPasswordValidator'},
]
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

STATIC_URL = 'static/'#example :localhost:8000/static/logo.png  ← une image statique

CORS_ALLOWED_ORIGINS = [
    'http://localhost:3000',  # ← React autorisé
]

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'