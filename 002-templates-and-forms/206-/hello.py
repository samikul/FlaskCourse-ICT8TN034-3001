## ei toimi vielä

from flask import Flask, render_template, request
app = Flask("__name__")

@app.route("/", methods=["POST", "GET"])
def index():
	print(request.form)
	return render_template("index.html", title="index")

if __name__ == '__main__':
	app.run()
