import pytz
from datetime import datetime
from flask_mail import Message
from flask import current_app
from datetime import timedelta
from project.host_services import mail, scheduler
from project.tools.reminder import Reminder


class Mailing:
    def __init__(self, reminder: Reminder):
        self.reminder = reminder
        self.mail = mail
        self.scheduler = scheduler
        self.app = current_app._get_current_object()
        self.one_hour_notification = None
        self.five_min_notification = None
        
    def _make_email_title(self, proximity: str) -> str:
        """
        Generates a title for a reminder email.
        """
        return f'Your event {self.reminder.event_name} is beginning {proximity}!'

    def _make_email_body(self) -> str:
        """
        Genearates a body text for a reminder email.
        """
        base = (f"\nYou are recieving this message because you have set a reminder in the Reminder app.")
        if self.reminder.commentary:
            return (base +
                    f"\nEvent comment:\n{self.reminder.commentary}")
        return base
    
    def _set_notification_datetimes(self) -> None:
        """
        Sets datetimes for sending reminder emails.
        """
        self.five_min_notification = self.reminder.reminder_datetime - timedelta(minutes=5)
        
        datetime_now = datetime.now(pytz.timezone(self.reminder.requested_timezone))
        one_hour_notification_datetime = self.reminder.reminder_datetime - timedelta(hours=1)
        
        if one_hour_notification_datetime > datetime_now:
            self.one_hour_notification = one_hour_notification_datetime

    def _send_notification(self, title_text: str, body_text: str) -> None:
        """
        Sends a reminder email.
        """
        message = Message(
            title_text,
            body=body_text,
            sender='your_email@mail.com',
            recipients=[self.reminder.user_email]
            )
        with self.app.app_context():
            self.mail.send(message=message)

    def _create_scheduler_job(self, run_date: datetime, text: str) -> None:
        """
        Schedules a job to send a notification email.
        """
        self.scheduler.add_job(id=None, func=self._send_notification,
                            run_date=run_date,
                            args=[self._make_email_title(text),
                            self._make_email_body()],
                            misfire_grace_time=3600)
        
    def schedule_notifications(self) -> None:
        """
        Schedules jobs for sending reminder emails.
        """
        self._set_notification_datetimes()
        self._create_scheduler_job(self.five_min_notification, "in 5 minutes")
        if self.one_hour_notification: 
            self._create_scheduler_job(self.one_hour_notification, "in an hour")