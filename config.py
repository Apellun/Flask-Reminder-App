from dotenv import load_dotenv

load_dotenv() #TODO: doesn't load
    
class Config:
    MAIL_SERVER='smtp.gmail.com'
    MAIL_PORT=587
    MAIL_USERNAME='mcinnie@gmail.com'
    MAIL_PASSWORD='zskzbbbzggiyeqry'
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False