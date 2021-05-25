from flask import Flask, render_template
app = Flask("__name__")

@app.route("/")
def index():
	colors = ["red", "blue", "green", "yellow"]
	return render_template("index.html", colors=colors, title="index")

@app.route("/foo")
def foo():
	return render_template("foo.html", title="foo")

app.run()
