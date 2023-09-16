import pytz
from datetime import datetime as dt, timedelta


class Reminder:
    def __init__(self, reminder_data, user_email):
        self.initial_timezone = reminder_data['initial_timezone']
        self.requested_timezone = reminder_data['requested_timezone']
        self.user_email = user_email
        self.event_name = reminder_data['event_name']
        self.commentary = reminder_data["commentary"]
        self.initial_datetime = reminder_data["initial_datetime"]
        self.reminder_datetime = None
        self.reminder_datetime_str = None
        self.one_hour_notification = False
    
    def convert_time(self, initial_time):
        initial_timezone = pytz.timezone(self.initial_timezone)
        requested_timezone = pytz.timezone(self.requested_timezone)
        event_time = initial_timezone.localize(initial_time, is_dst=None)
        return (event_time).astimezone(tz=requested_timezone)
    
    def check_notification_availability(self):
        five_mins_notification_deadline = dt.now(pytz.timezone(self.requested_timezone)) - timedelta(minutes=5)
        if self.reminder_datetime < five_mins_notification_deadline:
            raise ValueError
        one_hour_notification_deadline = dt.now(pytz.timezone(self.requested_timezone)) - timedelta(hours=1)
        if self.reminder_datetime > one_hour_notification_deadline:
            self.one_hour_notification = True
    
    def set_reminder_datetime(self):
        datetime = dt.strptime(
                self.initial_datetime,
                '%Y-%m-%dT%H:%M'
                )
        self.reminder_datetime = self.convert_time(datetime)
        self.reminder_datetime_str = dt.strftime(
            self.reminder_datetime,
            '%Y-%m-%d %H:%M'
            )