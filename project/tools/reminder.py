import pytz
from datetime import datetime, timedelta


class Reminder:
    def __init__(self, reminder_data):
        self.initial_timezone = reminder_data['initial_timezone']
        self.requested_timezone = reminder_data['requested_timezone']
        self.user_email = reminder_data['user_email']
        self.event_name = reminder_data['event_name']
        self.commentary = reminder_data["commentary"]
        self.initial_datetime_str = reminder_data["initial_datetime"]
        self.reminder_datetime = None
        self.reminder_datetime_str = None
        
    def _check_notification_possibility(self) -> None:
        """
        Checks if the requested datetime for the reminder is at least 5 minutes
        ahead of the current time.
        """
        datetime_now = datetime.now(pytz.timezone(self.requested_timezone))
        five_mins_notification_datetime = self.reminder_datetime - timedelta(minutes=5)
        if datetime_now > five_mins_notification_datetime:
            raise ValueError
    
    def _convert_datetime(self, initial_datetime: datetime) -> datetime:
        """
        Converts the datetime for the event from the initial timezone to
        the requested timezone.
        """
        initial_timezone = pytz.timezone(self.initial_timezone)
        requested_timezone = pytz.timezone(self.requested_timezone)
        event_time = initial_timezone.localize(initial_datetime, is_dst=None)
        
        return (event_time).astimezone(tz=requested_timezone)
        
    def _set_reminder_datetime(self):
        """
        Sets the reminder's datetime and the reminder's datetime in the srting format.
        """
        initial_datetime = datetime.strptime(
                self.initial_datetime_str,
                '%Y-%m-%dT%H:%M'
                )
        self.reminder_datetime = self._convert_datetime(initial_datetime)
        self.reminder_datetime_str = datetime.strftime(
            self.reminder_datetime,
            '%Y-%m-%d %H:%M'
            )
        
    def create(self):
        """
        Creates a Reminder.
        """
        self._set_reminder_datetime()
        try:
            self._check_notification_possibility()
        except ValueError as e:
            return e
        