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

	`$ git clone https://github.com/sindani254/SendIT-api_endpoints.git`
	
2. Checkout the _ch--integrate-test-coverage-reporting-161864049_

	`$ git checkout ch--integrate-test-coverage-reporting-161864049`

2. Install the dependencies

	`$ pip install requirements.txt`
	
3. Fire up server by running

	`$ python manage.py runserver`

## Usage
   ### _Base URL_
    
   _REQUEST_:
   
 	`[GET] http://127.0.0.1:5000/api/v1`
   
   _RESPONSE_:
   ``` 
   json
   {
       "welcome": "the-anonymous ni wale wase"
   }
   ```
------------------------------------------------

  ### _Get all parcel delivery orders endpoint_
  
   _REQUEST_:
   
 	`[GET] http://127.0.0.1:5000/api/v1/parcels
   
   _RESPONSE_:
   ```
   json
   {
       "all orders": [
           {
               "id": 1,
               "item_name": "Geforce GTX 1060 iGame",
               "origin": "nairobi cbd",
               "owner_id": 1,
               "pickup_location": "zimmerman base",
               "price": 45000,
               "status": "delivered"
           },
           {
               "id": 2,
               "item_name": "Geforce GTX 1080 ti",
               "origin": "nairobi cbd",
               "owner_id": 2,
               "pickup_location": "zimmerman base",
               "price": 105000,
               "status": "in transit"
           },
           {
               "id": 3,
               "item_name": "Geforce GTX 1050 ti",
               "origin": "nairobi cbd",
               "owner_id": 1,
               "pickup_location": "base",
               "price": 85000,
               "status": "cancelled"
           }
       ]
   }
   ```
   
------------------------------------------------

  ### _Get a particular parcel delivery order endpoint_
  
   _REQUEST_:
   
   `[GET] http://127.0.0.1:5000/api/v1/parcels/1`
   
   _RESPONSE_:
   ```
   json
   {
    "order details": [
        {
            "id": 1,
            "item_name": "Geforce GTX 1060 iGame",
            "origin": "nairobi cbd",
            "owner_id": 1,
            "pickup_location": "zimmerman base",
            "price": 45000,
            "status": "delivered"
        }
    ]
}
   ```
------------------------------------------------


  ### _Get a particular user's parcel delivery orders endpoint_
  
   _REQUEST_:
   
   `[GET] localhost:5000/api/v1/users/1/parcels`
   
   _RESPONSE_:
   ```
   json
   {
    "order details": [
            {
                "id": 1,
                "item_name": "Geforce GTX 1060 iGame",
                "origin": "nairobi cbd",
                "owner_id": 1,
                "pickup_location": "zimmerman base",
                "price": 45000,
                "status": "delivered"
            }
        ]
   }
   ```
------------------------------------------------

  ### _Post a parcel delivery order endpoint_
  
   _REQUEST_:
   
   ```
   [POST] http://127.0.0.1:5000/api/v1/parcels
   
   json
       {
	    "owner_id": 1,
	    "item_name": "Geforce GTX 1050",
	    "origin": "nairobi cbd",
	    "pickup_location": "base",
            "price": 85000
       }
   ```
   
   _RESPONSE_:
   
   ```
   json
   {
       "order details": {
	  "id": 4,
	  "item_name": "Geforce GTX 1050",
	  "origin": "nairobi cbd",
	  "owner_id": 1,
	  "pickup_location": "base",
	  "price": 85000,
	  "status": null
       }
   }
   ```
------------------------------------------------


  ### _Post a parcel delivery order endpoint_
  
   _REQUEST_:
   
   ```
   [POST] http://127.0.0.1:5000/api/v1/parcels
   
   json
       {
	    "owner_id": 1,
	    "item_name": "Geforce GTX 1050",
	    "origin": "nairobi cbd",
	    "pickup_location": "base",
            "price": 85000
       }
   ```
   
   _RESPONSE_:
   
   ```
   json
   {
       "order details": {
	  "id": 4,
	  "item_name": "Geforce GTX 1050",
	  "origin": "nairobi cbd",
	  "owner_id": 1,
	  "pickup_location": "base",
	  "price": 85000,
	  "status": null
       }
   }
   ```
------------------------------------------------


