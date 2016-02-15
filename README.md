# c-all-in

Call our announcement service and leave a message. This will later be played back using a 
public announcement (PA) system. If you want to create a call-recording service using Tropo's 
scripting API and Django, this repo might server as a good starting point. 

Uses Django 1.9 and Python 3.

# How to set up for development

Prerequisites: Install Python3 and virtualenvwrapper. 

1.  Clone this repository: `git clone ..`
2.  Setup your local Python3.3+ virtual environment: `mkvirtualenv -P python3 -a c-all-in/`
3.  Activate your virtual env: `workon c-all-in`
4.  Install requirements using `pip install -r requirments.txt`
5.  Run database migrations: `cd c_all_in ; ./manage.py migrate`
6.  Run the development server: `cd c_all_in ; ./manage.py runserver`
7.  Open up in Webbrowser: http://localhost:8000/

# How to set up for production

In order for this to work you need run this code on a public host on the internet. 
You also need to sign up for a Tropo account on https://www.tropo.com/.

1.  Create an account and login.
2.  Creat a new new Tropo application; choose 'Scripting API' as the application type.
3.  Enter the URL `http://<yourpublicservername>/calls/callmenu.py` in the input field `Voice Script` under `Script Details`.


------
Copyright (c) 2016 by Ansgar Schmidt, Uwe Kamper 