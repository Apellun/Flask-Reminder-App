import pytz
from datetime import timedelta
from flask import Flask, make_response, render_template, request
from flask_restx import Namespace, Resource, Api
from flask_mail import Mail, Message
from flask_apscheduler import APScheduler
import tools
from config import Config
from reminder import Reminder


app = Flask(__name__)
app.config.from_object(Config)
api = Api(app)
reminder_ns = Namespace('reminders/')
api.add_namespace(reminder_ns)
mail = Mail(app)
scheduler = APScheduler()
scheduler.init_app(app)
scheduler.start()


def send_notification(user_email, text, comment):
    message = Message(
        text,
        body=text + tools.make_email_body(comment),
        sender='your_email@mail.com',
        recipients=[user_email]
        )
    with app.app_context():
        mail.send(message=message)


def schedule_notifications(reminder):
    notification_datetime = reminder.reminder_datetime

    first_notification = notification_datetime - timedelta(hours=1)
    second_notification = notification_datetime - timedelta(minutes=5)

    scheduler.add_job(id=None, func=send_notification,
                        run_date=first_notification,
                        args=[reminder.user_email,
                        tools.make_email_title(reminder.event_name, "in an hour"),
                        reminder.commentary],
                        misfire_grace_time=3600)
    scheduler.add_job(id=None, func=send_notification,
                        run_date=second_notification,
                        args=[reminder.user_email,
                        tools.make_email_title(reminder.event_name, "in 5 minutes"),
                        reminder.commentary],
                        misfire_grace_time=3600)
    

@reminder_ns.route('/')
class ReminderView(Resource):
    def get(self):
        return make_response(render_template('index.html', timezones=list(pytz.common_timezones)))
    
    def post(self):
        data = request.form
        user_email = data["user_email"]
        
        reminder = Reminder(data, user_email)
        reminder.set_reminder_datetime()
        
        try:
            reminder.validate_time()
        except:
            return make_response(render_template('error.html'))
        
        schedule_notifications(reminder)
        return make_response(render_template('success.html',
                                             reminder_datetime=reminder.reminder_datetime_str,
                                             event_name=reminder.event_name,
                                             user_email=reminder.user_email,
                                             requested_timezone=reminder.requested_timezone))
   
        
if __name__ == '__main__':
    app.run()