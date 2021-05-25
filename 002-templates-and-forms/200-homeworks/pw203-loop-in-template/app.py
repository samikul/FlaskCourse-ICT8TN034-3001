from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def elements():
	elements = ["fire", "earth", "water", "air"]
	return render_template('elements.html', title="Elements", elements=elements)

app.run()
