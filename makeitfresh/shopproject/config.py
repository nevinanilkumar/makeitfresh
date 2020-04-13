# Change allowed hosts in user.routes login page before deploying


class Config:
    SECRET_KEY ='9b11ac4263069692c46bd2a3edefba42ede6837c'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///project.sqlite'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    BCRYPT_LOG_ROUNDS = 12

class Test:
    SECRET_KEY ='9b11ac4263069692c46bd2a3edefba42ede6837c'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.sqlite:'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TESTING = True
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    WTF_CSRF_ENABLED=False
    BCRYPT_LOG_ROUNDS = 12
