import requests
from flask import Flask
from flask import jsonify
from flask import json, request
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.config['MONGO_DBNAME'] = 'StarWars'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/StarWars'
app.config['JSON_SORT_KEYS'] = False

mongo = PyMongo(app)

planets = mongo.db.planets

#POST PLANET
@app.route('/planets', methods=['POST'])
def add_planet():
  try:
    name = request.json['name']
    climate = request.json['climate']
    terrain = request.json['terrain']
    films = get_filmes(name)
  except Exception as ex:
    return jsonify({'result' : 'Bad Request' , 'keyword': ex.args[0]}), 400
  planet_id = planets.insert({'name': name, 'climate': climate, 'terrain': terrain, 'films': films})
  p = planets.find_one({'_id': planet_id })
  output = ({'_id': str(p['_id']),'name': p['name'], 'climate': p['climate'], 'terrain':p['terrain'], 'filmes': p['films']})
  return jsonify({'result' : output})

#AUX FUNCTION GET FILMS
def get_filmes(name):
  url = "https://swapi.co/api/planets/?page=1"
  while(url is not None):
    response = requests.get(url)
    content = json.loads(response.content)
    results = content['results']
    next_url = content['next']
    for r in results:
      if(r['name']==name):
        return r['films']

    url = next_url
  return []

if __name__ == '__main__':
  app.run(debug=True)