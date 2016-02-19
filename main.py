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
	country = request.form['country']
	letter = request.form['letter']


	if name == '' or address1 == '' or address2 == '' or city == '' or state == '' or zipcode == '':
		return '<html><h1> Something is wrong with your request! make sure all fields are filled </h1></html>'
	if letter == ''
		return return '<html><h1> are you sure you want to send an empty letter? </h1></html>'
	#make api requests
	google_api_key = 'AIzaSyBYMVzqlYJHnOgknV-vShJv4zq77aQQYBw'
	lob.api_key = 'test_37e4de5759d46d675a12a7819f89fb08145'

	#get state representative
	request_string='https://www.googleapis.com/civicinfo/v2/representatives?address=' + state + '&levels=administrativeArea1&key=' + google_api_key
	

	try:
		response_data=json.load(urllib2.urlopen(request_string))
		to_zip = response_data['officials'][0]['address'][0]['zip']
		to_state = response_data['officials'][0]['address'][0]['state']
		to_city = response_data['officials'][0]['address'][0]['city']
		to_line1 = response_data['officials'][0]['address'][0]['line1']
		to_name = response_data['officials'][0]['name']
	except:
		return "taxation without representation"

	
	try:
		letter = lob.Letter.create(
		  description = 'Letter to state representative',
		  to_address = {
		      'name': to_name,
		      'address_line1': to_line1,
		      'address_city': to_city,
		      'address_state': to_state,
		      'address_zip': to_zip,
		      'address_country': 'US'
		  },
		  from_address = {
		      'name': name,
		      'address_line1': address1,
		      'address_city': city,
		      'address_state': state,
		      'address_zip': zipcode,
		      'address_country': 'US'
		  },
		  file = '<html style="padding-top: 3in; margin: .5in;">{{letter}}</html>',
		  data = {
		    'letter': letter
		  },
		  color = True
		)
	except:
		return "letter was not sent, try again and make sure everything is written correctly!"


	#return generated letter
	return redirect(letter['url'])


if __name__ == '__main__':
    app.run()