from datetime import timedelta

class Config:
    SEND_FILE_MAX_AGE_DEFAULT = 0
    SECRET_KEY = '579z1628bb0b13ce0c676dfde280ba245'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///data.db'
    PERMANENT_SESSION_LIFETIME =  timedelta(minutes=1440)
