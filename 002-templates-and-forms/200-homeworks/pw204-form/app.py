from flask import Flask, render_template
app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def form():
	return render_template('form.html', title="Form")

app.run()
