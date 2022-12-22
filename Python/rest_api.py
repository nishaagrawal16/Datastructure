# https://realpython.com/api-integration-in-python/#rest-architecture

import requests
import json


def get():
  api_url = "https://jsonplaceholder.typicode.com/todos/1"

  response = requests.get(api_url)

  print('\n****************************** Get ********************************')
  print('response: ', response)
  print('response.json(): ', response.json())

def post1():
  api_url = "https://jsonplaceholder.typicode.com/todos"

  data = {'userId': 2, 'title': 'test2', 'completed': False}
  headers = {'content-type': 'application/json'}
  response = requests.post(api_url, data=json.dumps(data), headers=headers)

  print('\n****************************** Post *******************************')
  print('response: ', response)
  print('response.json(): ', response.json())

def post2():
  api_url = "https://jsonplaceholder.typicode.com/todos"

  data = {'userId': 3, 'title': 'test3', 'completed': False}
  response = requests.post(api_url, json=data)

  print('\n**************************** Post json ****************************')
  print('response: ', response)
  print('response.json(): ', response.json())

def put():
    api_url = "https://jsonplaceholder.typicode.com/todos/1"

    data = {'userId': 4, 'title': 'test4', 'completed': False}
    response = requests.put(api_url, json=data)

    print('\n****************************** Put ******************************')
    print('response: ', response)
    print('response.json(): ', response.json())

def patch():
    api_url = "https://jsonplaceholder.typicode.com/todos/1"

    data = {'title': 'test5'}
    response = requests.patch(api_url, json=data)

    print('\n****************************** Patch ****************************')
    print('response: ', response)
    print('response.json(): ', response.json())

def delete():
    api_url = "https://jsonplaceholder.typicode.com/todos/1"

    response = requests.delete(api_url)

    print('\n****************************** Delete ***************************')
    print('response: ', response)
    print('response.json(): ', response.json())

if __name__ == '__main__':
  get()
  post1()
  post2()
  put()
  patch()
  delete()
