# c-all-in

Call our announcement service and leave a message. This will later be played back using a 
public announcement (PA) system.

# How to set up for development

Prerequisites: Install Python3 and virtualenvwrapper

1.  Clone this repository: `git clone ..`
2.  Setup your local Python3.3+ virtual environment: `mkvirtualenv -P python3 -a c-all-in/`
3.  Activate your virtual env: `workon c-all-in`
4.  Install requirements using `pip install -r requirments.txt`
5.  Run database migrations: `cd c_all_in ; ./manage.py migrate`
6.  Run the development server: `cd c_all_in ; ./manage.py runserver`
7.  Open up in Webbrowser: http://localhost:8000/
