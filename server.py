from flask import Flask
from flask_restx import Namespace, Api
from flask_mail import Mail
from flask_apscheduler import APScheduler


def create_app_and_services(config):
    app = Flask(__name__)
    app.config.from_object(config)
    api = Api(app)
    reminder_ns = Namespace('reminder/')
    api.add_namespace(reminder_ns)
    mail = Mail(app)
    scheduler = APScheduler()
    scheduler.init_app(app)
    scheduler.start()
    
    return app, mail, scheduler, reminder_ns