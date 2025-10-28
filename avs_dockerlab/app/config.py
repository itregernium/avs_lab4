import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'qwerty21322'
    POSTGRES_USER = os.environ.get('POSTGRES_USER')
    POSTGRES_PASSWORD = os.environ.get('POSTGRES_PASSWORD')
    POSTGRES_DB = os.environ.get('POSTGRES_DB')
    POSTGRES_HOST = os.environ.get('POSTGRES_HOST')
    
    SQLALCHEMY_DATABASE_URI = (
        f'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@'
        f'{POSTGRES_HOST}:5432/{POSTGRES_DB}'
    )
    
    # не трогать
    SQLALCHEMY_TRACK_MODIFICATIONS = False