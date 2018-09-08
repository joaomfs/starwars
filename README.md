# starwars-planets

Simple REST API designed to store Star Wars planets, written in Python using Flask and MongoDB database.

## Running the project

To run this project, first we need to prepare the environment:
```
* virtualenv flask
* cd flask
* pip3 install flask
* pip3 install markupsafe
* pip install flask-pymongo
* pip install requests

```

And create a MongoDB database called 'StarWars'

Then, run the starwars-planets.py
```
* python starwars-planets.py
```

## Using Postman

You can use an tool like [Postman](https://www.getpostman.com/).
The planets sent to API must follow the following JSON format:

```
{
    "name": "Cato Neimoidia",
    "climate": temperate, moist",
    "terrain": "mountains, fields, forests, rock arches"
}
```

To Update, you only need to send the fields you want to update.

The API will get the movies apparitions from the named planet, if exists, and will persist in the database.

You can use the following endpoints with the API:

Insert a new planet:
* POST - http://127.0.0.1:5000/planets

List all planets:
* GET - http://127.0.0.1:5000/planets

Search a planet by name:
* GET - http://127.0.0.1:5000/planets/name/{name}

Search a planet by id:
* GET - http://127.0.0.1:5000/planets/{id}

Update a planet by id:
* PUT - http://127.0.0.1:5000/planets/{id}

Remove a planet:
* DELETE - http://127.0.0.1:5000/planets/{id}


## Built With

* [SWAPI](https://swapi.co/)

## Authors

* **João Freitas**
