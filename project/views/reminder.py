import pytz
from flask_restx import Namespace
from flask import make_response, render_template, request
from flask_restx import Resource
from project.services.reminder import Reminder
from project.services.mailing import Mailing

reminder_ns = Namespace('reminder/')

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
        
        mailing = Mailing(reminder)
        mailing.schedule_notifications()
        
        return make_response(render_template('success.html',
                                             reminder_datetime=reminder.reminder_datetime_str,
                                             event_name=reminder.event_name,
                                             user_email=reminder.user_email,
                                             requested_timezone=reminder.requested_timezone))