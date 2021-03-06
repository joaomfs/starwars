import requests
from flask import Flask, jsonify, json, request
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.config['MONGO_DBNAME'] = 'starwars'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/starwars'
app.config['JSON_SORT_KEYS'] = False

mongo = PyMongo(app)

planets = mongo.db.planets

@app.route('/', methods=['GET'])
def help():
  msg = "Insert a new planet:\n * POST - http://127.0.0.1:5000/planets\n "
  msg += "List all planets:\n * GET - http://127.0.0.1:5000/planets\n"
  msg+= "Search a planet by name: \n * GET - http://127.0.0.1:5000/planets?name={name}\n"
  msg+= "Search a planet by id: \n * GET - http://127.0.0.1:5000/planets/{id}\n"
  msg+= "Update a planet by id: \n * PUT - http://127.0.0.1:5000/planets/{id}\n"
  msg+= "Remove a planet:\n * DELETE - http://127.0.0.1:5000/planets/{id}"
  return msg

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

#GET PLANET BY NAME
@app.route('/planets', methods=['GET'])
def get_planet_by_name():
  name = request.args.get('name')
  if(name is None):
    return get_all_planets()
  fplanets = planets.find({'name': name})
  if planets.count_documents({'name':name})==0:
    return jsonify({'result': 'Planet not found'}), 404
  output =[]
  for p in fplanets:
    output.append({'_id': str(p['_id']),'name': p['name'], 'climate': p['climate'], 'terrain':p['terrain'], 'filmes': p['films']})
  return jsonify({'result': output})

#GET PLANET BY ID
@app.route('/planets/<id>', methods=['GET'])
def get_planet_by_id(id):
  try:
    p = planets.find_one({'_id': ObjectId(id)})
  except Exception as ex:
    return jsonify({'result' : 'Bad Request' , 'keyword': ex.args[0]}), 400
  if p is None:
    return jsonify({'result': 'Planet not found'}), 404
  output = ({'_id': str(p['_id']),'name': p['name'], 'climate': p['climate'], 'terrain':p['terrain'], 'filmes': p['films']})
  return jsonify({'result': output})

#UPDATE PLANET
@app.route('/planets/<id>', methods=['PUT'])
def update_planet(id):
  try:
    p = planets.find_one({'_id': ObjectId(id)})
  except Exception as ex:
    return jsonify({'result' : 'Bad Request' , 'keyword': ex.args[0]}), 400
  if p is None:
    return jsonify({'result': 'Planet not found'}), 404    

  try:
    name = request.json['name']
    p['name'] = name
  except Exception:
    p['name'] = p['name']
  try:
    climate = request.json['climate']
    p['climate'] = climate
  except Exception:
    p['climate'] = p['climate']
  try:
    terrain = request.json['terrain']
    p['terrain'] = terrain
  except Exception:
    p['terrain'] = p['terrain']

  films = get_filmes(p['name'])
  p['films'] = films

  planets.save(p)
  output = ({'_id': str(p['_id']),'name': p['name'], 'climate': p['climate'], 'terrain':p['terrain'], 'filmes': p['films']})
  return jsonify({'result': output})

#DELETE PLANET
@app.route('/planets/<id>', methods=['DELETE'])
def delete_planet(id):
  try:
    p = planets.find_one({'_id': ObjectId(id)})
  except Exception as ex:
    return jsonify({'result' : 'Bad Request' , 'keyword': ex.args[0]}), 400
  if p is None:
    return jsonify({'result': 'Planet not found'}), 404

  planets.remove(p)
  return jsonify({'result': 'Deleted'})

#GET ALL PLANETS
def get_all_planets():
  fplanets = planets.find()
  output =[]
  for p in fplanets:
    output.append({'_id': str(p['_id']),'name': p['name'], 'climate': p['climate'], 'terrain':p['terrain'], 'filmes': p['films']})

  return jsonify({'result': output})


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