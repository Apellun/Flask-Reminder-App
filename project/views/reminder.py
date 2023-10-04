import pytz
from flask_restx import Namespace
from flask import make_response, render_template, request
from flask_restx import Resource
from project.services import reminder_service

reminder_ns = Namespace('reminder/')


@reminder_ns.route('/')
class ReminderView(Resource):
    def get(self):
        return make_response(render_template('index.html', timezones=list(pytz.common_timezones)))
    
    def post(self):
        event = reminder_service.set_reminder(request.form)
        if not event:
            return make_response(render_template('error.html'))
        return make_response(render_template('success.html',
                                             reminder_datetime=event.reminder_datetime_str,
                                             event_name=event.event_name,
                                             user_email=event.user_email,
                                             requested_timezone=event.requested_timezone))