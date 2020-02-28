import sys
import webapp2
import mysql.connector
from mysql.connector import Error
class userInfo(webapp2.RequestHandler):
    def get(self):
        print('User Info')
        try:
            connection = mysql.connector.connect(host='localhost',
                                                 database='temp',
                                                 user='root',
                                                 password='root')
            print('connection: ', connection)
            if connection.is_connected():
                db_Info = connection.get_server_info()
                print("Connected to MySQL Server version ", db_Info)
                cursor = connection.cursor()
                cursor.execute("select database();")
                record = cursor.fetchone()
                print("You're connected to database: ", record)
                # sql = "INSERT INTO employe (name, id) VALUES (%s, %s)"
                # val = ("John", "2")
                # cursor.execute(sql, val)
                sql = "DELETE FROM employe WHERE id=2"
                cursor.execute(sql)
                connection.commit()
                print(cursor.rowcount, "record inserted.")
                cursor.execute("SELECT * FROM employe")
                myresult = cursor.fetchall()
                for x in myresult:
                    print(x)

        except Error as e:
            print("Error while connecting to MySQL", e)
        finally:
            if (connection.is_connected()):
                cursor.close()
                connection.close()
                print("MySQL connection is closed")
        self.response.headers.add_header('Access-Control-Allow-Origin', '*')
        self.response.headers['Content-Type'] = 'application/json'
        self.response.write('Nisha Agrawal')
        sys.stdout.flush()

# """This module provides generic utility functions for handling API requests."""
# 
# from __future__ import google_type_annotations
# 
# import json
# import typing
# import webapp2
# 
# class userInfo(base_handler.BaseHandler):
# class BaseHandler(webapp2.RequestHandler):
#   """Provides common functions to request handler subclasses."""
# 
#   def _succeed(self, msg: str = '', data: typing.Any = None):
#     return self._set_response(success=True, msg=msg, data=data)
# 
#   def _fail(self, msg: str = ''):
#     return self._set_response(success=False, msg=msg)
# 
#   def _set_response(self, **kwargs: typing.Any):
#     self.response.headers['Content-Type'] = 'text/json'
#     output = json.dumps(kwargs)
#     self.response.out.write(output)