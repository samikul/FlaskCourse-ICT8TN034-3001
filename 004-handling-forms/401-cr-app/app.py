from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

from flask_wtf import FlaskForm # m
from wtforms.ext.sqlalchemy.orm import model_form # m

app = Flask(__name__)
app.secret_key = "joleeficaeghieR9xohzeitohquei2"
db = SQLAlchemy(app)

class Color(db.Model): # m
	id = db.Column(db.Integer, primary_key=True) # m
	name = db.Column(db.String, nullable=False)

ColorForm = model_form(Color, base_class=FlaskForm, db_session=db.session) # m

@app.before_first_request
def initDB():
	db.create_all() # m

	color = Color(name="Blue")
	db.session.add(color) # m

	color = Color(name="Red")
	db.session.add(color)

	color = Color(name="Yellow")
	db.session.add(color)

	color = Color(name="Green")
	db.session.add(color)

	db.session.commit() # m

@app.route("/")
def colors():
	colors = Color.query.all() # m
	return render_template("colors.html", colors=colors)

@app.route("/new", methods=["GET", "POST"])
def new():
	form = ColorForm() # m

	if form.validate_on_submit(): # m the whole if-block
		color = Color()
		form.populate_obj(color)

		db.session.add(color)
		db.session.commit()

		print("Color added.")

	return render_template("new.html", form=form)

if __name__ == "__main__":
	app.run()
