# Reminder app

<p><b>Technologies:</b> Flask, Flaks-mail, Flask-appscheduler.</p>

## How to run:

1. Download the app folder to your computer.
2. Fill in the example.env file and rename it into .env.
3. From the project folder in the terminal, run:
`pip install -r requirements.txt`
`flask run`

This is a simple app I built for myself. It allows the user to set a reminder for an event, for a datetime in another timezone. The app converts the datetime from the original timezone to the requested timezone and sends reminders to the user's email: one an hor before and another one five minutes before ther selected datetime. If a user requests a reminder for the time that is less than one hour in the future, the user recieves only one email. If the user selects the datetime in the past, reminder is not created and the app asks to pick another time.

<p><b>The endpoint for setting a reminder:</b> localhost:port/reminder/</p>

I built this app to help myself keep track of the events I had to be present on that happenned in a different timezone.

## Challenges

I had trouble with the app's architecture: I wanted to separate the views, tool functions and the reminders logic. But every time it came to the same circular import issue, since to use the mail and the scheduler I couldn't just get them from the app context — I had to use the exact instances I create with the app initialization. I've yet to find a way to go around this issue, for now I decided the best way to go is to just keep everything in one module.