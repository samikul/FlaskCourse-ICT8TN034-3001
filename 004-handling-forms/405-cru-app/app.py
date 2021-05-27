from flask import Flask, render_template, redirect, flash
from flask_sqlalchemy import SQLAlchemy

from flask_wtf import FlaskForm
from wtforms.ext.sqlalchemy.orm import model_form # m

app = Flask(__name__)
app.secret_key = "ongaeth2Xie7aiv1efio5ohchiehei"
db = SQLAlchemy(app)

class Character(db.Model): # m
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String, nullable=False)

CharacterForm = model_form(Character, base_class=FlaskForm, db_session=db.session) # m

@app.before_first_request # m
def initDB():
	db.create_all()

	character = Character(name="Mikki Hiiri")
	db.session.add(character) # m

	character = Character(name="Aku Ankka")
	db.session.add(character)

	character = Character(name="Hessu Hopo")
	db.session.add(character)

	db.session.commit()

@app.route("/")
def characters():
	characters = Character.query.all() # m
	return render_template("characters.html", characters=characters)

@app.route("/<int:id>/edit", methods=["GET", "POST"])
@app.route("/new", methods=["GET", "POST"])
def newCharacter(id=None):
	character = Character()
	if id:
		character = Character.query.get_or_404(id)
	
	form = CharacterForm(obj=character)

	if form.validate_on_submit(): # m the whole if block
		form.populate_obj(character)

		db.session.add(character)
		db.session.commit()

		flash("Character added")
		return redirect("/")

	return render_template("new.html", form=form)

if __name__ == "__main__":
	app.run()
