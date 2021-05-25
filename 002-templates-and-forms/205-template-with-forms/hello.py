from flask import Flask, render_template
app = Flask("__name__")

@app.route("/", methods=["GET", "POST"])
def index():
	return render_template("index.html", title="index")

@app.route("/foo", methods=["GET", "POST"])
def foo():
	return render_template("foo.html", title="foo")

@app.route("/bar", methods=["GET", "POST"])
def bar():
	return render_template("bar.html", title="bar")

if __name__ == '__main__':
	app.run()
