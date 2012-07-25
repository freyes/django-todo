django-todo
===========

[![Build Status](https://secure.travis-ci.org/frameworktodo/django-todo.png?branch=master)](http://travis-ci.org/frameworktodo/django-todo)


### Installation

If you don't already, install [Python 2.7.3](http://www.python.org/download/). Now install the `pip` and `virtualenv` commands.

```bash
sudo easy_install pip
sudo pip install virtualenv
```

You're now clear to checkout the project.

```bash
git clone https://github.com/frameworktodo/django-todo.git
cd django-todo
```

Go ahead and install the application dependencies.

```bash
virtualenv venv --distribute
source venv/bin/activate
pip install -r requirements.txt
```

You should be able to access the project in the browser at http://localhost:8000.

In order to interact with tasks, you'll want to setup the database.

```bash
python manage.py syncdb
```
