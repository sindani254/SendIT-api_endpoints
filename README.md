[![Build Status](https://travis-ci.org/sindani254/SendIT-endpoints.svg?branch=master)](https://travis-ci.org/sindani254/SendIT-endpoints)
# SendIT - Flask-RESTful API endpoints
This project shows one of the possible ways to implement RESTful API server.

There are two implemented models: User and Todo, one user has many todos.

## _Main libraries used_:
1. Flask-Migrate - for handling all database migrations.
2. Flask-RESTful - restful API library.
3. Flask-Script - provides support for writing external scripts.

## _Project structure_:
```
.
|-- README.md
|-- __init__.py
|-- __pycache__
|   |-- app.cpython-37.pyc
|   |-- config.cpython-37.pyc
|   |-- models.cpython-37.pyc
|   `-- tests.cpython-37.pyc
|-- app
|   |-- __init__.py
|   |-- __pycache__
|   |   `-- __init__.cpython-37.pyc
|   |-- api
|   |   |-- __init__.py
|   |   |-- __pycache__
|   |   |   `-- __init__.cpython-37.pyc
|   |   `-- v1
|   |       |-- __init__.py
|   |       |-- __pycache__
|   |       |   |-- __init__.cpython-37.pyc
|   |       |   |-- models.cpython-37.pyc
|   |       |   `-- views.cpython-37.pyc
|   |       |-- models.py
|   |       `-- views.py
|   |-- requirements.txt
|   `-- run.py
|-- coverage
|   |-- app_api_v1_views_py.html
|   |-- coverage_html.js
|   |-- index.html
|   |-- jquery.ba-throttle-debounce.min.js
|   |-- jquery.hotkeys.js
|   |-- jquery.isonscreen.js
|   |-- jquery.min.js
|   |-- jquery.tablesorter.min.js
|   |-- keybd_closed.png
|   |-- keybd_open.png
|   |-- status.json
|   `-- style.css
|-- instance
|   |-- __init__.py
|   |-- __pycache__
|   |   |-- __init__.cpython-37.pyc
|   |   `-- config.cpython-37.pyc
|   `-- config.py
|-- manage.py
|-- requirements.txt
|-- run.py
`-- tests
    |-- __init__.py
    |-- __pycache__
    |   |-- __init__.cpython-37.pyc
    |   `-- test_views.cpython-37.pyc
    `-- test_views.py

12 directories, 41 files
```

* app - holds all endpoints.
* run.py - flask application initialization.
* tests - holds all test codes.
* coverage - holds coverage reports.
* manage.py - script for managing application (migrations, server execution, etc.)

## Running 

1. Clone repository.

	`git clone https://github.com/sindani254/SendIT-api_endpoints.git`

2. Install the dependencies

	`pip install requirements.txt`
	
3. Start server by running

	`$ python manage.py runserver`

## Usage
   ### Base URL 
    
   _REQUEST_:
	
   - [GET] http://127.0.0.1:5000/api/v1
   
   _RESPONSE_:
   ``` 
   json
   {
	    "welcome": "crackers ni wale wase"
   }
   ```
------------------------------------------------
  ### Get all parcel delivery orders endpoint
  
  _REQUEST_:
	
   - [GET] http://127.0.0.1:5000/api/v1
   
   _RESPONSE_:
   ``` 
   json
   {
	    "welcome": "crackers ni wale wase"
   }
   ```
------------------------------------------------
  
  
  
PUT http://127.0.0.1:5000/api/users/1

REQUEST
```json
{
	"name": "Smith Smith"
}
```
RESPONSE
```json
{
    "id": 1,
    "name": "Smith Smith",
    "todos": []
}
```
DELETE http://127.0.0.1:5000/api/users/1

RESPONSE
```json
{
    "id": 3,
    "name": "Tom Tom",
    "todos": []
}
```
GET http://127.0.0.1:5000/api/users

RESPONSE
```json
{
    "count": 2,
    "users": [
        {
            "id": 1,
            "name": "John John",
            "todos": [
                {
                    "id": 1,
                    "name": "First task",
                    "description": "First task description"
                },
                {
                    "id": 2,
                    "name": "Second task",
                    "description": "Second task description"
                }
            ]
        },
        {
            "id": 2,
            "name": "Smith Smith",
            "todos": []
        }
    ]
}
```
GET http://127.0.0.1:5000/api/users/2
```json
{
    "id": 2,
    "name": "Smith Smith",
    "todos": []
}
```
GET http://127.0.0.1:5000/api/users?name=John John
```json
{
    "count": 1,
    "users": [
        {
            "id": 1,
            "name": "John John",
            "todos": [
                {
                    "id": 1,
                    "name": "First task",
                    "description": "First task description"
                },
                {
                    "id": 2,
                    "name": "Second task",
                    "description": "Second task description"
                }
            ]
        }
    ]
}
```
GET http://127.0.0.1:5000/api/users?limit=1&offset=1
```json
{
    "count": 1,
    "users": [
        {
            "id": 2,
            "name": "Smith Smith",
            "todos": []
        }
    ]
}
```

