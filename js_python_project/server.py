#!/usr/
import webapp2
import user_info

class HelloWebapp2(webapp2.RequestHandler):
    def get(self):
        print('I am here')
        self.response.headers.add_header('Access-Control-Allow-Origin', '*')
        self.response.headers['Content-Type'] = 'application/json'
        self.response.write('Hello, webapp2!')

app = webapp2.WSGIApplication([
    ('/', HelloWebapp2),
    ('/user_info', user_info.userInfo),
], debug=True)

def main():
    from paste import httpserver
    httpserver.serve(app, host='127.0.0.1', port='8082')

if __name__ == '__main__':
    main()
