from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
	return render_template('index.html', title="Index", hello="Hello", world="world!")

app.run()
