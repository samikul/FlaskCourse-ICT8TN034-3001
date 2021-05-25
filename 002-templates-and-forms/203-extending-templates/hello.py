from flask import Flask, render_template
app = Flask("__name__")

@app.route("/")
def index():
	return render_template("index.html", title="index")

@app.route("/foo")
def foo():
	return render_template("foo.html", title="foo")

@app.route("/bar")
def bar():
	return render_template("bar.html", title="bar")

app.run()
