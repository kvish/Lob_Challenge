from flask import Flask
from flask import request, render_template, redirect, url_for, redirect
import json

app = Flask(__name__)
app.config.from_object(__name__)


#homepage acts at form for letter
@app.route('/')
def index():
	return render_template('index.html')

@app.route('/send', methods = ['POST'])
def send():
	#return "send letter"
	name = request.form['name']
	address1 = request.form['address1']
	address2 = request.form['address2']
	city = request.form['city']
	state = request.form['state']
	zipcode = request.form['zip']
	letter = request.form['letter']

	return name + address1 + address2 + city + state + zipcode + letter
	


if __name__ == '__main__':
    app.run()