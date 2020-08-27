from user import User

def authenticate(username, password):
  user = User.find_by_username(username)
  if user and user.password == password:
    return user

def identity(payload):
  print('payload: ', payload)
  user_id = payload['identity']
  print('user_id: ', user_id)
  return User.find_by_id(user_id)
