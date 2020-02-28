import webapp2
class userInfo(webapp2.RequestHandler):
    def get(self):
        print('I am here')
        # form_data = json.loads(self.request.body)
        self.response.headers.add_header('Access-Control-Allow-Origin', '*')
        self.response.headers['Content-Type'] = 'application/json'
        self.response.write('Nisha Agrawal')

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