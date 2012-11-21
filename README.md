seg4105-ccms
============

Rapid prototype for the Computer Corner Management System for Liam Peyton's Project Management Class at the University of Ottawa.

Installation
------------

Installing and configuring the CCMS Demo is fairly simple.  The basic steps
are to create a virtual environment, install the required packages, and sync
the database.  To get started:

    $ cd /source/directory/
    $ virtualenv -p python2.7 venv
    $ source ./venv/bin/activate
    $ pip install -r requirements.txt
    $ ./manage.py syncdb
    $ ./manage.py migrate

There you go!

Development Server
------------------

To run the development server locally, execute:

    $ source ./venv/bin/activate
    $ ./manage.py runserver

