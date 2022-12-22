from flask import Flask, request, jsonify

app = Flask(__name__)

countries = [
    {"id": 1, "name": "Thailand", "capital": "Bangkok", "area": 513120},
    {"id": 2, "name": "Australia", "capital": "Canberra", "area": 7617930},
    {"id": 3, "name": "Egypt", "capital": "Cairo", "area": 1010408},
]

# curl http://127.0.0.1:5000/countries
@app.get('/countries')
def get_countries():
  return jsonify(countries)
# In get_countries(), you need to use jsonify() because you’re returning a list
# of dictionaries and not just a single dictionary. Flask doesn’t automatically
# convert lists to JSON.

# curl http://127.0.0.1:5000/country/1
@app.get('/country/<id>')
def get_country(id):
  return countries[int(id)]

def _find_next_id():
  return max([country['id'] for country in countries]) + 1

# curl http://127.0.0.1:5000/countries -X POST -H 'Content-Type: application/json' -d '{"name": "India", "capital": "Delhi", "area": 1234567}'
@app.post('/countries')
def add_country():
  if request.is_json:
    country_data = request.get_json()
    country_data['id'] = _find_next_id()
    countries.append(country_data)
    return country_data, 201
  return {'error': 'Request must be json'}, 415
