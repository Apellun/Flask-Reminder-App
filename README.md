<i>Ридми на русском — ниже.</i>
# Reminder app

<p><b>Technologies:</b> Flask, Flaks-mail, Flask-appscheduler.</p>

## How to run:

1. Download the app folder to your computer.
2. Fill in the example.env file and rename it into .env.
3. From the project folder in the terminal, run:<br>
`pip install -r requirements.txt`<br>
`flask run`

This is a simple app I built for myself. It allows the user to set a reminder for an event, for a datetime in another timezone. The app converts the datetime from the original timezone to the requested timezone and sends reminders to the user's email: one an hour before and another one five minutes before the selected datetime. If a user requests a reminder for a time that is less than one hour in the future, the user receives only one email. If the user selects the datetime in the past, reminder is not created and the app asks to pick another time.

<p><b>The endpoint for setting a reminder:</b> localhost:port/reminder/</p>

I built this app to help myself keep track of the events I had to be present on that happened in a different timezone.

## Challenges

I had trouble with the app's architecture: I wanted to separate the views, tool functions and the reminders logic. But every time it came to the same circular import issue, since to use the mail and the scheduler I couldn't just get them from the app context — I had to use the exact instances I was creating with the app initialization. I've yet to find a way to go around this issue, for now, I decided the best way to go is to just keep everything in one module.

# Reminder app

<p><b>Technologies:</b> Flask, Flaks-mail, Flask-appscheduler.</p>

## How to run:

1. Download the app folder to your computer.
2. Fill in the example.env file and rename it into .env.
3. From the project folder in the terminal, run:<br>
`pip install -r requirements.txt`<br>
`flask run`

This is a simple app I built for myself. It allows the user to set a reminder for an event, for a datetime in another timezone. The app converts the datetime from the original timezone to the requested timezone and sends reminders to the user's email: one an hor before and another one five minutes before ther selected datetime. If a user requests a reminder for the time that is less than one hour in the future, the user recieves only one email. If the user selects the datetime in the past, reminder is not created and the app asks to pick another time.

<p><b>The endpoint for setting a reminder:</b> localhost:port/reminder/</p>

I built this app to help myself keep track of the events I had to be present on that happenned in a different timezone.

## Challenges

I had trouble with the app's architecture. I wanted to put the views, tool functions and reminders logic into different modules. But every time I encountered the same circular import issue, since to use the mail and the scheduler functionality I couldn't just get them from the app context — I had to use the exact instances I was creating with the app initialization. I've yet to find a way to go around this issue, for now, I decided to just keep most logic in one module.

## Functionality I am planning to add in the future

1) Simple convertation of time from one timezone to another.
2) The ability for user to receive reminders in Whatsapp, maybe also in Telegram.

<i>Here starts the Readme in Russian.</i>

# Приложение Напоминалка

<p><b>Технологии:</b> Flask, Flaks-mail, Flask-appscheduler.</p>

## Как запустить:

1. Скопируйте репозиторий на компьютер
2. Заполните example.env и переименуйте его в .env.
3. Из папки проекта в терминале запустите команды:<br>
`pip install -r requirements.txt`<br>
`flask run`

Это простое приложение, я собрала его для себя. Приложение позволяет пользователю установить напоминалку для какого-то события, с датой-временем в отличном от его часовом поясе. Приложение конвертирует дату-время в дату-время в часовом поясе ползователя и отправляет напоминалку на почту пользователя: одну за час до события и еще одну за пять минут. Если пользователь запрашивает напоминалку для события, которое начинается меньше, чем через час, он получит тольк одно письмо. Если пользователь выбирает дату-время в прошлом, напоминалка не создается, а приложение просит пользователя выбрать другое время.

<p><b>Адрес для создания напоминалки:</b> localhost:port/reminder/</p>

Я собрала это приложение, чтобы мне было удобнее следить за событиями, которые требовали моего присутствия, но проходили по времени другого часового пояса (например, московского).

## Трудности

У меня возникли проблемы с архитектурой приложения. Я хотела разделить вью, служебные функции и логику напоминалок на модули. Но каждый раз натыкалась на проблему циклического импорта, потому что чтобы использовать функциональность mail и scheduler я не могла просто получить их из контектса приложения — мне нужны были именно объекты, которые я создавала при инициализации приложения. Я до сих пор пытаюсь решить эту проблему. А пока я решила просто оставить большую часть логики в одном модуле.

## Функционал, который я планирую добавить в будущем

1) Просто конвертация времени из одного часового пояса в другой.
2) Возможность получать напоминалки в Whatsapp, может быть еще в Telegram.
