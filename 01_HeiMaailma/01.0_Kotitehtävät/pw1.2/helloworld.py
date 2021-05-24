from flask import Flask

app = Flask("__name__")

@app.route("/")
def helloflask():
	return "Hello Flaskworld!\n"

app.run()
