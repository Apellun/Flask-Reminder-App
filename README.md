<i>Ридми на русском — ниже.</i>
# Reminder app

Web-app created with Flask. Sends emails reminding about the events happening in another time zone by the user’s requested time zone time.

Uses Flask-APScheduler and Flask-Mail, Has a simple HTML-interface.

<p><b>The endpoint for setting a reminder:</b> localhost:port/reminder/</p>

## How to run:

1. Download the repository to your computer.
2. Fill in the project/example.env file and rename it into .env.
3. From the project folder in the terminal, run:<br>
`pip install -r requirements.txt`<br>
`flask run`

## Challenges

For a long time, I had trouble with the app's structure. I wanted to separate the views, the tool functions, and the services into different modules. But every time I tried, I ran into the circular import issue connected to the mail and the scheduler objects initialization. Right now I've managed to solve it.

## Functionality I am planning to add in the future

1) Simple convertation of time from one timezone to another.
2) The ability for users to receive reminders in Whatsapp, maybe also in Telegram.
3) The ability for users to view their schedule in the app.

<i>Here starts the Readme in Russian.</i>

# Приложение Напоминалка

Веб-приложение на Flask. Отправляет электронные письма с напоминанием о событиях в другой временной зоне по времени временной зоны, запрошенной пользователем.

Использует Flask-APScheduler и Flask-Mail, есть простой HTML-интерфейс.

<p><b>Адрес для создания напоминалки:</b> localhost:port/reminder/</p>

## Как запустить:

1. Скопируйте репозиторий на компьютер.
2. Заполните project/example.env и переименуйте его в .env
3. Из папки project проекта в терминале запустите команды:<br>
`pip install -r requirements.txt`<br>
`flask run`

## Трудности

Долгое время у меня были проблемы со структурой приложения. Я хотела разделить вью, служебные функции и сервисы на модули. Но каждый раз, когда я пыталась это сделать, я натыкалась на проблему циклического импорта, связанного с инициализацией объектов mail и scheduler. На данный момент я с этим разобралась.

## Функционал, который я планирую добавить в будущем

1) Простая конвертация даты-времени из одного часового пояса в другой.
2) Возможность получать напоминалки в Whatsapp, может быть еще в Telegram.
3) Возможность для пользователей просматривать свое расписание в приложении.
