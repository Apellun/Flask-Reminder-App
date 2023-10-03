import os
from dotenv import load_dotenv

load_dotenv()
    
class Config:
    MAIL_SERVER = str(os.getenv('MAIL_SERVER'))
    MAIL_PORT = (os.getenv('MAIL_PORT'))
    MAIL_USERNAME = str(os.getenv('MAIL_USERNAME'))
    MAIL_PASSWORD = str(os.getenv('MAIL_PASSWORD'))
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    FLASK_DEBUG = str(os.getenv('FLASK_DEBUG'))