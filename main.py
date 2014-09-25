import webapp2
from timeline import Timeline

timeline = Timeline()
timeline.get_data_from_local_csv()

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
