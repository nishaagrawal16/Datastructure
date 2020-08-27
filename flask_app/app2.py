# Lint as: python3
"""TODO(nishaa): DO NOT SUBMIT without one-line documentation for app2.

TODO(nishaa): DO NOT SUBMIT without a detailed description of app2.
"""
from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required
from security import authenticate, identity

app = Flask(__name__)
app.secret_key = 'jose'
api = Api(app)

jwt = JWT(app, authenticate, identity) #/auth
items = []

class Item(Resource):
  # This is only for parse the request payload from the frontend
  # and skip other not useful data.
  parser = reqparse.RequestParser()
  parser.add_argument('price',
    type=float,
    required=True,
    help="This filed can not be left blank!"      
  )
  @jwt_required()
  def get(self, name):
    # filter returns the list of values as object so we are using
    # next method for geting the 1st value from the list.
    item = next(filter(lambda x: x['name'] == name, items), None)
    # for item in items:
      # if item['name'] == name:
        # return item
    return {'item': item}, 200 if item else 404

  def post(self, name):
    if next(filter(lambda x: x['name'] == name, items), None):
      return {'message': "An item with name '{}' is already exists.".format(name)}, 400
    data = Item.parser.parse_args()
    new_item = {
        'name': name,
        'price': data['price']
    }
    items.append(new_item)
    return new_item, 201

  def put(self, name):
    # This is the one of the way to delete the item form the list.
    # request_data = request.get_json()
    # for item in items:
    #   if item['name'] == name:
    #     item['price'] = request_data['price']
    #     return item

    # This only send the data which is given as "price".
    # If we added another data with price e.g: 
    # {
    #   "price": 12.33,
    #   "name": "hello"
    # }
    # It will skip the name parameter as this is not mentioned in the parser.
    data = Item.parser.parse_args()
    item = next(filter(lambda x: x['name'] == name, items), None)
    if item is None:
      items.append({'name': name, 'price': data['price']})
    else:
      item.update(data)
    return item

  def delete(self, name):
    # This is the one of the way to delete the item form the list.
    # for i in range(len(items)):
    #   if items[i]['name'] == name:
    #     del items[i]
    #     return items
    global items
    items = list(filter(lambda x: x['name'] != name, items))
    return {'message': 'Item deleted'}

class ItemList(Resource):
  def get(self):
    return {'items': items }


api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')


if __name__ == '__main__':
  app.run(port=5000, debug=True)
