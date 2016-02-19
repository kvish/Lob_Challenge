from flask import Flask
from flask import request, render_template, redirect, url_for, redirect
import json

app = Flask(__name__)

@app.route('/')
def Letter():
	return "Lob Coding Challenge"


if __name__ == '__main__':
    app.run()