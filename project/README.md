<i>Ридми на русском — ниже.</i>
# Reminder app

<p><b>Technologies:</b> Flask, Flaks-mail, Flask-appscheduler.</p>

## How to run:

1. Download the app folder to your computer.
2. Fill in the example.env file and rename it into .env.
3. From the project folder in the terminal, run:<br>
`pip install -r requirements.txt`<br>
`flask run`

This is a simple app I built for myself. It allows the user to keep track of the events in different time zones. The app converts the datetime to the user's selected time zone and sends reminders to the user's email: one an hour before and another five minutes before the event. If a user requests a reminder for a time that is less than one hour in the future, the user receives only one reminder. If the user selects the datetime in the past, a reminder is not created and the app asks them to pick another time.

<p><b>The endpoint for setting a reminder:</b> localhost:port/reminder/</p>

## Challenges

I had trouble with the app's architecture: I wanted to separate the views, the tool functions, and the reminders logic into different modules. But every I tried I ran into the same circular import issue, since to use the mail and the scheduler I had to use the exact instances created with the app initialization. I've yet to find a way to go around this issue, for now, I decided that the best way to go is to just keep everything in one module.

## Functionality I am planning to add in the future

1) Simple convertation of time from one timezone to another.
2) The ability for users to receive reminders in Whatsapp, maybe also in Telegram.
3) The ability for users to view their schedule in the app.

<i>Here starts the Readme in Russian.</i>

# Приложение Напоминалка

<p><b>Технологии:</b> Flask, Flaks-mail, Flask-appscheduler.</p>

## Как запустить:

1. Скопируйте репозиторий на компьютер
2. Заполните example.env и переименуйте его в .env.
3. Из папки проекта в терминале запустите команды:<br>
`pip install -r requirements.txt`<br>
`flask run`

Это простое приложение, которое я собрала для себя. Оно помогоает пользователю уследить за событиями в разных часовых поясах. Приложение конвертирует введенную дату-время в дату-время в часовом поясе, заданном ползователем, и отправляет напоминалку ему на почту: одну за час до события и еще одну за пять минут. Если пользователь запрашивает напоминалку для события, которое начинается меньше, чем через час, он получает только одно письмо. Если пользователь выбирает дату-время в прошлом, напоминалка не создается, а приложение просит пользователя выбрать другое время.

<p><b>Адрес для создания напоминалки:</b> localhost:port/reminder/</p>

## Трудности

У меня возникли проблемы с архитектурой приложения. Я хотела разделить вью, служебные функции и логику напоминалок на модули. Но каждый раз, когда я пыталась это сделать, я натыкалась на проблему циклического импорта, ведь, чтобы использовать функциональность mail и scheduler, мне нужны были объекты, которые создаются при инициализации приложения. Я до сих пор пытаюсь решить эту проблему. Пока просто оставила большую часть логики в одном модуле.

## Функционал, который я планирую добавить в будущем

1) Простая конвертация даты-времени из одного часового пояса в другой.
2) Возможность получать напоминалки в Whatsapp, может быть еще в Telegram.
3) Возможность для пользователей просматривать свое расписание в приложении.