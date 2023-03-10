import os


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY')
    DB_NAME = os.getenv('DATABASE')
    APP_ID = os.getenv('APY_ID')
    UPLOAD_FOLDER = os.path.join('app', 'static', 'img', 'profile')
    UPLOAD_URL = '/static/img/profile/'
    ALLOWED_EXTENSIONS = {'png', 'jpeg', 'gif'}

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig,
}
