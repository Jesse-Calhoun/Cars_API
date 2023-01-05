# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-m9cjtca2#zn$m143t3&x--l^+s9eu83t0$7tw2(qd3ved1^lw0'

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': 'cars_database',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': 'Jimafer2736!'
    }
}