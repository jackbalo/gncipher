import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # Configure session to use filesystem (instead of signed cookies)
    SESSION_PERMANENT = os.getenv("SESSION_PERMANENT")
    SESSION_TYPE = os.getenv("SESSION_TYPE")
    SESSION_COOKIE_SECURE= os.getenv("SESSION_COOKIE_SECURE")
    SESSION_COOKIE_HTTPONLY = os.getenv("SESSION_COOKIE_HTTPONLY")
    SESSION_COOKIE_SAMESITE = os.getenv('SESSION_COOKIE_SAMESITE')
    PERMANENT_SESSION_LIFETIME = os.getenv("PERMANENT_SESSION_LIFETIME") # 30 minutes

    SECRET_KEY = os.getenv("SECRET_KEY")
    SECURITY_PASSWORD_SALT = os.getenv("SECURITY_PASSWORD_SALT")

    SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # list of google scopes - https://developers.google.com/identity/protocols/oauth2/scopes

    GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
    GOOGLE_CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET")
    GOOGLE_SCOPE = os.getenv("GOOGLE_SCOPE")
    GOOGLE_META_URL = os.getenv("GOOGLE_META_URL")

    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_SERVER = os.getenv("MAIL_SERVER")
    MAIL_PORT = 465
    MAIL_USERNAME =  os.getenv("MAIL_USERNAME")
    MAIL_PASSWORD =  os.getenv("MAIL_PASSWORD")
    MAIL_DEFAULT_SENDER = os.getenv("MAIL_DEFAULT_SENDER")
