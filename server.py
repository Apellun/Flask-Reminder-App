from flask import Flask
from flask_restx import Api
from services import mail, scheduler
from views import reminder_ns

def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    api = Api(app)
    api.add_namespace(reminder_ns)
    scheduler.init_app(app)
    scheduler.start()
    mail.init_app(app)
    
    return app