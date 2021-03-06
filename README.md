# starwars-planets

Simple REST API designed to store Star Wars planets, written in Python using Flask and MongoDB database.

## Running the project

To run this project you need a database called 'starwars' in a MongoDB server running on port 27017 on localhost.

Or, you can use the deployed database at MongoDB Atlas by changing the app.config['MONGO_URI'] to 'mongodb+srv://skywalker:maytheforcebewithyou@cluster0-z7w6h.mongodb.net/starwars?retryWrites=true'

then prepare the environment and run:
```
* pip install -r requirements.txt
* python starwars-planets.py
```

## Using Postman

You can use a tool like [Postman](https://www.getpostman.com/).
The planets sent to the API must follow the following JSON format:

```
{
    "name": "Cato Neimoidia",
    "climate": "temperate, moist",
    "terrain": "mountains, fields, forests, rock arches"
}
```

To Update you only need to send the fields you want to update.

The API will get the list of movies the named planet appeared, if exists, and will persist in the database.

You can use the following endpoints with the API:

Insert a new planet:
* POST - http://127.0.0.1:5000/planets

List all planets:
* GET - http://127.0.0.1:5000/planets

Search a planet by name:
* GET - http://127.0.0.1:5000/planets?name={name}

Search a planet by id:
* GET - http://127.0.0.1:5000/planets/{id}

Update a planet by id:
* PUT - http://127.0.0.1:5000/planets/{id}

Remove a planet by id:
* DELETE - http://127.0.0.1:5000/planets/{id}


## Built With

* [SWAPI](https://swapi.co/)

## Authors

* **João Freitas**
