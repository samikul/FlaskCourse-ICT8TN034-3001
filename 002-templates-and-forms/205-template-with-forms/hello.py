from flask import Flask, render_template
app = Flask("__name__")

@app.route("/", methods=["POST", "GET"])
def index():
	return render_template("index.html", title="index")

@app.route("/foo", methods=["POST", "GET"])
def foo():
	return render_template("foo.html", title="foo")

@app.route("/bar", methods=["POST", "GET"])
def bar():
	return render_template("bar.html", title="bar")

if __name__ == '__main__':
	app.run()
