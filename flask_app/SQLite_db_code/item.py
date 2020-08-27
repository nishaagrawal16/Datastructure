import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required

class Item(Resource):
  # This is only for parse the request payload from the frontend
  # and skip other not useful data.
  parser = reqparse.RequestParser()
  parser.add_argument('price',
    type=float,
    required=True,
    help="This filed can not be left blank!"      
  )

  @classmethod
  def find_by_name(cls, name):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    query = "SELECT * FROM items where name=?"
    cursor.execute(query, (name,))
    row = cursor.fetchone()
    connection.close()

    if row:
      return {'item': {'name': row[0], 'price': row[1]}}

  @classmethod
  def insert(cls, item):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    
    insert_query = "INSERT INTO items VALUES (?, ?)"
    cursor.execute(insert_query, (item['name'], item['price']))
    connection.commit()
    connection.close()

  @classmethod
  def update(cls, item):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    
    update_query = "UPDATE items SET price = ? WHERE name=?"
    cursor.execute(update_query, (item['price'], item['name']))
    connection.commit()
    connection.close()

  @jwt_required()
  def get(self, name):
    item = Item.find_by_name(name)
    if item:
      return item
    return {'message': 'Item not found'}, 404

  def post(self, name):
    item = Item.find_by_name(name)
    if item:
      return {'message': "An item with name '{}' is already exists.".format(name)}, 400
    data = Item.parser.parse_args()
    item = {
        'name': name,
        'price': data['price']
    }
    try:
      Item.insert(item)
    except:
      return {'message': 'An error occured inserting the item'}, 500 # Internal server error
    return item, 201

  def put(self, name):
    data = Item.parser.parse_args()
    updated_item = {
        'name': name,
        'price': data['price']
    }    
    item = Item.find_by_name(name)
    if item:
      try:
        Item.update(updated_item)
      except:
        return {'message': 'An error occured updating the item'}, 500
    else:
      try:
        Item.insert(updated_item)
      except:
        return {'message': 'An error occured inserting the item'}, 500
    
    return updated_item

  def delete(self, name):
    item = Item.find_by_name(name)
    if item:
      connection = sqlite3.connect('data.db')
      cursor = connection.cursor()
      delete_query = "DELETE FROM items where name=?"
      cursor.execute(delete_query, (name,))
      connection.commit()
      connection.close()
      return {'message': 'Item deleted'}
    return {'message': 'Item not found'}

class ItemList(Resource):
  def get(self):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    query = "SELECT * FROM items"
    cursor.execute(query)
    row = cursor.fetchall()
    connection.close()
    return {'items': row}