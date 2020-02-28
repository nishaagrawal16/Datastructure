import json
import webapp2
import sys
class employeData(webapp2.RequestHandler):
    def post(self):
        # print('I am here in employe data: ', self.request)
        # print('self.request.body: ', self.request.body)
        print('Employee Info')
        form_data = json.loads(self.request.body)
        print('form_data: ', form_data)

        self.response.headers.add_header('Access-Control-Allow-Origin', '*')
        self.response.headers['Content-Type'] = 'application/json'
        self.response.write('Nisha Agrawal employee data')
        sys.stdout.flush()

