from flask import Flask
from flask import request, render_template, redirect, url_for, redirect
import json
import lob
import urllib
import urllib2

app = Flask(__name__)
app.config.from_object(__name__)


#homepage acts at form for letter
@app.route('/')
def index():
	return render_template('index.html')

@app.route('/send', methods = ['POST'])
def send():
	
	#access form data
	name = request.form['name']
	address1 = request.form['address1']
	address2 = request.form['address2']
	city = request.form['city']
	state = request.form['state']
	zipcode = request.form['zip']
	letter = request.form['letter']


	if name == '' or address1 == '' or address2 == '' or city == '' or state == '' or zipcode == '':
		return '<html><h1> Something is wrong with your request! make sure all fields are filled </h1></html>'
	
	#make api requests
	google_api_key = 'AIzaSyB7Ei3b6IIMhv1udluKomljDwBcJeZSIgQ'
	lob.api_key = 'test_37e4de5759d46d675a12a7819f89fb08145'


	letter = lob.Letter.create(
	  description = 'Demo Letter',
	  to_address = {
	      'name': 'Harry Zhang',
	      'address_line1': '123 Test Street',
	      'address_city': 'Mountain View',
	      'address_state': 'CA',
	      'address_zip': '94041',
	      'address_country': 'US'
	  },
	  from_address = {
	      'name': 'Harry Zhang',
	      'address_line1': '123 Test Avenue',
	      'address_city': 'Seattle',
	      'address_state': 'WA',
	      'address_zip': '94041',
	      'address_country': 'US'
	  },
	  file = '<html style="padding-top: 3in; margin: .5in;">HTML Letter for {{name}}</html>',
	  data = {
	    'name': 'Harry'
	  },
	  color = True
	)


	return redirect(letter['url'])


if __name__ == '__main__':
    app.run()