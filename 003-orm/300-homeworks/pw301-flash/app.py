from flask import Flask, render_template, flash, redirect # sudo apt-get install -y python3-flask

app = Flask(__name__)
app.secret_key = "angohd8nai5cagee7weivu8xiu7Nur"

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/about")
def about():
	return render_template("about.html")

@app.route("/portfolio")
def portfolio():
	return render_template("portfolio.html")

@app.route("/contact")
def contact():
	return render_template("contact.html")

@app.route("/flash")
def notification():
	flash("Hello flash message!")
	return redirect("/")

@app.route("/msg")
def message():
	flash("Hello another flash message!")
	return redirect("/")

if __name__ == "__main__":
	app.run()
