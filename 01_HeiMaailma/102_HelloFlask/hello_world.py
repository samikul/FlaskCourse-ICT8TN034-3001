from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello flask!"

@app.route("/foo")
def foo():
    return "foo"

@app.route("/bar")
def bar():
    return "bar"

app.run()
