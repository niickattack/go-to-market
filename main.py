import webapp2

form = """
<form method = "post">
	What is your birthday?
	<br>
	<br>
	<label> Month
	<input type = 'text' name = 'month'>
	</label>
	<label> Day
	<input type = 'text' name = 'day'>
	</label>
	<label> Year
	<input type = 'text' name = 'year'>
	</label>
	<br>
	<br>
	<input type = 'submit'>
</form>
"""

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.out.write(form)

    def post(self):
    	self.response.out.write("Thanks! That's a totally valid day!")

app = webapp2.WSGIApplication([
	('/', MainHandler),
	], debug=True)
