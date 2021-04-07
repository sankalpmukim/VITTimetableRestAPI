# VIT Calendar API
 A simple Flask based REST API to generate json containing timetable calendar data

Find official API user instructions [here](https://documenter.getpostman.com/view/15245880/TzCS6S6S)

## How its built?
 - The app runs on a very basic instance of the [Flask](https://flask.palletsprojects.com/en/1.1.x/) web framework.
 - It generates an ics file format code using the [icalendar](https://pypi.org/project/icalendar/) python module.

## How it works?
The API requires a JSON object containing whole site data of VTOP timetable page. It parses this data and looks for certain keys to make sense of it. As it understands the user's subscribed courses and their slots, it registers them as separate events and using simple logic plots those events on a weekly cycling calendar. This information can be used to write a .ics file with icalendar module. That .ics file can be imported into any major calendar service by the following methods.
 - [Google Calendar](https://support.google.com/calendar/thread/3231927?hl=en&msgid=3236002)
 - [Apple Calendar](https://www.techwalla.com/articles/how-to-add-an-ics-calendar-to-iphone-ipod-touch-or-ipad)
 - [Outlook](https://support.microsoft.com/en-us/office/import-calendars-into-outlook-8e8364e1-400e-4c0f-a573-fe76b5a2d379)