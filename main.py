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
	<br> <br> <br>
	<input type = 'submit'>
</form>
"""

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.out.write(form)

    months = ['January',
          'February',
          'March',
          'April',
          'May',
          'June',
          'July',
          'August',
          'September',
          'October',
          'November',
          'December']

	def valid_month(month):
	    if month:
	        cap_month = month.capitalize()
	        if cap_month in months:
	            return cap_month

	def valid_day(day):
    	if day and day.isdigit():
        	day = int(day)
        	if day >= 1 and day<= 31:
            	return day

    def valid_year(year):
    	if year and year.isdigit():
        	if int(year) >= 1900 and int(year) <=2020:
            	return int(year)


    def post(self):
    	user_month = valid_month(self.request.get('month'))
    	user_day = valid_day(self.request.get('day'))
    	user_year = valid_year(self.request.get('year')

    	if not (user_year and user_month and user_day):
    		self.response.out.write(form)
    	else:
    		self.response.out.write("Thanks!  That's a totally vaild day")

app = webapp2.WSGIApplication([
	('/', MainHandler),
	], debug=True)
