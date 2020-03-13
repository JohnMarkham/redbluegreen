from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
def index():
	return "Hello World"

@app.route("/<string:name>")
def hello(name):
	print(name)
	return "Gello {0}".format(name.capitalize())
