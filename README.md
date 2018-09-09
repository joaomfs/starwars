# starwars-planets

Simple REST API designed to store Star Wars planets, written in Python using Flask and MongoDB database.

## Running the project

For running this project you need a database called StarWars in a MongoDB server running on port 27017 on localhost.

Or, you can use de deployed database at MongoDB Atlas changing the app.config['MONGO_URI'] to 'mongodb+srv://skywalker:maytheforcebewithyou@cluster0-z7w6h.mongodb.net/starwars?retryWrites=true'

To run this project, first you need to prepare the environment:
```
* pip install -r requirements.txt
* python starwars-planets.py
```

And create a MongoDB database called 'StarWars'
## Using Postman

You can use an tool like [Postman](https://www.getpostman.com/).
The planets sent to API must follow the following JSON format:

```
{
    "name": "Cato Neimoidia",
    "climate": "temperate, moist",
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
* GET - http://127.0.0.1:5000/planets?name={name}

Search a planet by id:
* GET - http://127.0.0.1:5000/planets?id={id}

Update a planet by id:
* PUT - http://127.0.0.1:5000/planets?id={id}

Remove a planet by id:
* DELETE - http://127.0.0.1:5000/planets?id={id}


## Built With

* [SWAPI](https://swapi.co/)

## Authors

* **João Freitas**
