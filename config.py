import os

class Config:
    '''
    General configuration parent class
    '''
    QUOTE_API_BASE_URL = 'http://quotes.stormconsultancy.co.uk/random.json (Links to an external site.)'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://clarisse:1234@localhost/myblog'
    SECRET_KEY='123'
    # UPLOADED_PHOTOS_DEST ='app/static/photos'
    #  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = "klaryc4@gmail.com"
    MAIL_PASSWORD = "bienvenido"
    
    # simple mde  configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True

class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    
# class TestConfig(config):
#     SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://clarisse:123@localhost//blogstest'
        
class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True    

config_options ={
    'development':DevConfig,
    'production':ProdConfig,
    # 'test':TestConfig
}