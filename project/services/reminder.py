import pytz
from datetime import datetime, timedelta


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
    
    def convert_time(self, initial_time):
        initial_timezone = pytz.timezone(self.initial_timezone)
        requested_timezone = pytz.timezone(self.requested_timezone)
        event_time = initial_timezone.localize(initial_time, is_dst=None)
        return (event_time).astimezone(tz=requested_timezone)
    
    def check_notification_availability(self):
        datetime_now = datetime.now(pytz.timezone(self.requested_timezone))
        five_mins_notification_datetime = self.reminder_datetime - timedelta(minutes=5)
        if datetime_now > five_mins_notification_datetime:
            raise ValueError
    
    def set_reminder_datetime(self):
        initial_datetime_str = datetime.strptime(
                self.initial_datetime,
                '%Y-%m-%dT%H:%M'
                )
        self.reminder_datetime = self.convert_time(initial_datetime_str)
        self.reminder_datetime_str = datetime.strftime(
            self.reminder_datetime,
            '%Y-%m-%d %H:%M'
            )