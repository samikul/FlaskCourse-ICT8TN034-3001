from flask import Flask, render_template
app = Flask("__name__")

@app.route("/")
def index():
	colors = ["red", "blue", "green", "yellow"]
	return render_template("index.html", colors=colors, title="index")

@app.route("/foo")
def foo():
	animals = ["monkey", "elephant", "kangaroo", "koala"]
	return render_template("foo.html", animals=animals, title="foo")

@app.route("/bar")
def bar():
	return render_template("bar.html", title="bar")

app.run()
