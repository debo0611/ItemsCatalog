# Udacity Items Catalog Project

Welcome to the Items catalog project. This project is created as a part of Udacity full stack nanodegree. It is a web application to be run on a browser and also provides a few REST endpoints to check existing categories and items.


## Tools/technology used:
- python3
- Flask
- PostgreSQL
- SQLAlchemy
- Jinja2
- Bootstrap
- REST API creation/testing


## Prerequisites:

Most of the python packages are already installed in the Udacity fullstack VM.
Some additional flask extensions that were used for developing the project are:

- Flask-Bootstrap
- Flask-HTTPAuth
- Flask-Login
- Flask-WTF
- Flask-SQLAlchemy


## Installation 

The project is developed in the catalog folder provided in the VM, so repository needs to be cloned in the local system and made available to the catalog folder.

1. Download the fullstack nanodegree VM provided by Udacity
2. vagrant up
3. vagrant ssh
4. Inside the fullstack/vagrant/catalog folder (in the local system), clone this repo: <p> git clone https://github.com/debo0611/ItemsCatalog.git </p>

Note that 'vagrant' is the folder shared between the local system and the VM.
5. Access the catalog folder from the VM (accessed via vagrant ssh)

6. Database used/created (in the VM) is "catalog". (This db need to be pre-created)
Two tables are created in the above db (they will be created, if not already created, when the application runs):
a. ‘catalog’ (should have been named 'category')
b. 'item’

## Usage: 
Command to start the application: 
$ python3 run.py 

Access it in browser:
<p> http://localhost:8080/ </p>

Access REST API endpoints using a REST client (like POSTMAN):

- 127.0.0.1:8080/categories  — get all created categories
- 127.0.0.1:8080/category/<category_id>  — get category by <category_id>
- 127.0.0.1:8080/items  - get all the items
- 127.0.0.1:8080/item/<item_id> - get specific item by <item_id>


## Caveat:

If the user is logged in for a long time, there can be an issue with logout:
Please use the below url to login a different user:
<p> http://localhost:8080/login </p>