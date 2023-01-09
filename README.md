# Flask_studying
learning flask
Site where you can view the current weather and a 5-day forecast for cities, you can create your own list of cities, view the weather for capitals.

This application has:

For an unregistered user:
Application "Test user":
- the ability to fill the database with a test list of users,
- the ability to add a user,
- the ability to delete a user,
- the ability to edit user data

For registered users:
Application "Weather":
- everything for an unregistered user,
plus
source of weather information - https://openweathermap.org/
- the ability to view the current weather in the city,
- the ability to add a city to the database of cities,
- the ability to fill an empty database of cities with a list of randomly selected cities from countries (Ukraine, USA, Japan, Great Britain, Australia),
- the ability to fill an empty database of capitals with a list of randomly selected 25 capitals,
- the ability to select cities by country,
- the ability to watch the weather forecast for 5 days,
- Ability to remove cities from the list.

For start project.
Create file .flaskenv in base dir with next info:

FLASK_APP=web.py
FLASK_DEBUG=1
SECRET_KEY=
ENVIRONMENT=development
DATABASE=user.db
APY_ID=
FLASK_RUN_PORT=
QTY_PER_PAGE=10

You must add data after =:
SECRET_KEY=, APY_ID=, FLASK_RUN_PORT=
APY_ID you must get on site https://openweathermap.org/
