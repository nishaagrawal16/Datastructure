from paste import httpserver
import webapp2
import employe_data
import user_info
import sys

class HelloWebapp2(webapp2.RequestHandler):
    def get(self):        
        print('In HelloWebapp2 get***')   
        self.response.headers.add_header('Access-Control-Allow-Origin', '*')
        self.response.headers['Content-Type'] = 'application/json'
        self.response.write('Hello, webapp2!')
        sys.stdout.flush()

app = webapp2.WSGIApplication([
    ('/', HelloWebapp2),
    ('/user_info', user_info.userInfo),
    ('/employe_data', employe_data.employeData),
], debug=True)

def main():
    httpserver.serve(app, host='127.0.0.1', port='8082')

if __name__ == '__main__':
    main()
# C:\Users\disha\AppData\Local\Programs\Python\Python37\;
