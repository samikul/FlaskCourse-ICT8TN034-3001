from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
	return "Hello\n"

@app.route("/foo")
def foo():
	return "foo\n"

@app.route("/bar")
def bar():
	return "bar\n"

app.run()
