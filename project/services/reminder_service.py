from project.tools.reminder import Reminder
from project.tools.mailing import Mailing


class ReminderService:
    def set_reminder(data):
        reminder = Reminder(data)
        try:
            reminder.create()
        except ValueError:
            return None
        
        mailing = Mailing(reminder)
        mailing.schedule_notifications()
        
        return reminder