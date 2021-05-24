## Based on code written by Tero Karvinen, 2020
## https://terokarvinen.com//2020/flask-templates/
## Visit Tero's website terokarvinen.com

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("base.html", greeting="Hello world!")

app.run(debug=True)
