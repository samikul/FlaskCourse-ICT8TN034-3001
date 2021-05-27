from flask import Flask, render_template, redirect, flash # sudo apt-get install -y python3-flask
from flask_sqlalchemy import SQLAlchemy # sudo apt-get install -y python3-flask-sqlalchemy

from flask_wtf import FlaskForm
from wtforms.ext.sqlalchemy.orm import model_form # sudo apt-get install -y python3-flaskext.wtf

app = Flask(__name__)
app.secret_key = "oviey4haeheijiXoh1needeegh3aeY"
db = SQLAlchemy(app)

class Contact(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	firstname = db.Column(db.String, nullable=False)
	lastname = db.Column(db.String, nullable=False)
	mobile = db.Column(db.String, nullable=False)
	email = db.Column(db.String)
	streetaddress = db.Column(db.String)
	postalcode = db.Column(db.String)
	city = db.Column(db.String)

ContactForm = model_form(Contact, base_class=FlaskForm, db_session=db.session)

@app.before_first_request
def initDB():
	db.create_all()

	contact = Contact(firstname="Maija", lastname="Meikäläinen", mobile="+358500000000",
				email="maija@email.com", streetaddress="Kotikatu 123",
				postalcode="00100", city="Helsinki")
	db.session.add(contact)

	contact = Contact(firstname="Matti", lastname="Meikäläinen", mobile="+358451111111",
				email="matti@email.com", streetaddress="Pääkatu 3 a 8",
				postalcode="00590", city="Helsinki")
	db.session.add(contact)

	contact = Contact(firstname="Erkki", lastname="Esimerkki", mobile="+358402222222",
				email="erkki@email.com", streetaddress="Polku 2 b 2",
				postalcode="33100", city="Tampere")
	db.session.add(contact)

	contact = Contact(firstname="Enni", lastname="Esimerkki", mobile="+35853333333",
				email="enni@email.com", streetaddress="Tie 7",
				postalcode="20100", city="Turku")
	db.session.add(contact)

	db.session.commit()

@app.route("/")
def contacts():
	contacts = Contact.query.all()
	return render_template("contacts.html", contacts=contacts)

@app.route("/<int:id>/edit", methods=["GET", "POST"])
@app.route("/new", methods=["GET", "POST"])
def newContact(id=None):
	contact = Contact()
	if id:
		contact = Contact.query.get_or_404(id)

	form = ContactForm(obj=contact)

	if form.validate_on_submit():
		form.populate_obj(contact)

		db.session.add(contact)
		db.session.commit()

		flash("Added")
		return redirect("/")

	return render_template("new.html", form=form)

@app.route("/<int:id>/delete")
def deleteContact(id):
	contact = Contact.query.get_or_404(id)
	db.session.delete(contact)
	db.session.commit()

	flash("Deleted")
	return redirect("/")

if __name__ == "__main__":
	app.run()
