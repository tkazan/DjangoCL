# Django CL Project

This project consists of 2 separate apps:
### 1. BookConferenceRoomApp
which is an app for booking a conference room

### 2. DjangoCLApp
which is just for Django training

<hr>

#### REQUIREMENTS - How to start working with that project (on Ubuntu):
1. Check if you have a <b>Python 3.5</b> installed:<br/> 
$ python3 --version | if not: <br/>
$ sudo apt-get update <br/>
$ sudo apt-get install python3
2. Check if you have <b>pip3</b> installed: <br/> 
$ pip3 --version | if not: <br/> 
$ sudo apt-get install -y python3-pip
3. Check if you have <b>virtualenv</b> installed: <br/>
$ virtualenv --version | if not: <br/>
$ pip3 install virtualenv
4. Check if you have <b>PostgreSQL</b> installed: <br/>
$ psql --version | if not: <br/>
$ sudo apt-get install postgresql postgresql-contrib
<br/> -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-
5. Clone a repository on your PC
6. Create a new PostgreSQL database: DjangoCLdb
7. Create and activate a new virtenv: <br/>
$ virtualenv -p python3 DjangoVirtEnv <br/>
$ source DjangoVirtEnv/bin/activate
8. Install requirements: <br/>
(Django==1.11.6, psycopg2) <br/>
$ pip3 install -r requirements.txt
9. Run a database backup file: <br/>
$ psql -U postgres -f DjangoCLdb.sql -h localhost DjangoCLdb
10. Make migrations: <br/>
$ python manage.py makemigrations <br/>
$ python manage.py migrate
11. Runserver: <br/>
$ python manage.py runserver
12. Use the django app on url: <br/>
<a href="http://localhost:8000/bookconfroom/">http://localhost:8000/bookconfroom/</a>


