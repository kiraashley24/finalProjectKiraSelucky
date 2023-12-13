# Final Project

INF 601 - Advanced Programming with Python -
Kira Selucky
-----

## Description
This project uses Django, Bootstrap, and character name & age API to display D&D website with D&D information and character building. 
-----

## Pip install instructions

Please run the following:

```
pip install -r requirements.txt
```



-----
## How to run this project
In a terminal window, please type the following:
```
python manage.py
python manage.py migrate
python manage.py makemigrations
python manage.py createsuperuser
python manage.py runserver
``` 
-----
## Details on each command line
1. *python manage.py* - server environment, django-admin, sets DJANGO_SETTINGS_MODULE that points to project's settings.py 
2. *python manage.py migrate* - initializes database and creates tables
3. *python manage.py makemigrations* - applies changes to models
4. *python manage.py createsuperuser* - creates admin profile
5. *python manage.py runserver* - runs server to launch website
-----
## Web pages 

1. Home - index page
2. Races page - displays different Race options
3. Classes page - displays different Class Options
4. Character Builder page - where registration/login appears, then shows build form
5. Character page showing character selections