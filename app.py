import pytz
from datetime import timedelta
from flask import make_response, render_template, request
from flask_restx import Resource
from flask_mail import Message
import tools
from config import Config
from reminder import Reminder
from server import create_app_and_services


app, mail, scheduler, reminder_ns = create_app_and_services(Config)


def send_notification(user_email: str, text: str, comment: str) -> None:
    """
    Sends a reminder email.
    """
    message = Message(
        text,
        body=text + tools.make_email_body(comment),
        sender='your_email@mail.com',
        recipients=[user_email]
        )
    with app.app_context():
        mail.send(message=message)


def schedule_notifications(reminder: Reminder) -> None:
    """
    Schedules jobs for sending reminder emails.
    """
    notification_datetime = reminder.reminder_datetime
    one_hour_notification = notification_datetime - timedelta(hours=1)
    five_min_notification = notification_datetime - timedelta(minutes=5)

    scheduler.add_job(id=None, func=send_notification,
                        run_date=five_min_notification,
                        args=[reminder.user_email,
                        tools.make_email_title(reminder.event_name, "in 5 minutes"),
                        reminder.commentary],
                        misfire_grace_time=3600)
    
    if reminder.one_hour_notification:
        scheduler.add_job(id=None, func=send_notification,
                            run_date=one_hour_notification,
                            args=[reminder.user_email,
                            tools.make_email_title(reminder.event_name, "in an hour"),
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
            reminder.check_notification_availability()
        except:
            return make_response(render_template('error.html'))
        
        schedule_notifications(reminder)
        return make_response(render_template('success.html',
                                             reminder_datetime=reminder.reminder_datetime_str,
                                             event_name=reminder.event_name,
                                             user_email=reminder.user_email,
                                             requested_timezone=reminder.requested_timezone))