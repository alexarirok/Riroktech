import os

class Config:
    SECRET_KEY = "8c7e01d62ca49b"
    SQLALCHEMY_DATABASE_URI = "postgresql://alex:postgres@localhost/tech"
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'akorir233@gmail.com'
    MAIL_PASSWORD = 'Korir1920$$'