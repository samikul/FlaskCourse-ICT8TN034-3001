from flask import Flask, render_template, redirect, flash # sudo apt-get install -y python3-flask
from flask_sqlalchemy import SQLAlchemy # sudo apt-get install -y python3-flask-sqlalchemy

from flask_wtf import FlaskForm
from wtforms.ext.sqlalchemy.orm import model_form # sudo apt-get install -y python3-flaskext.wtf

app = Flask(__name__)
app.secret_key = "aijaish4epoopheSa6chit5xoa7eer"
db = SQLAlchemy(app)

class Reply(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String, nullable=False)
	email = db.Column(db.String, nullable=False)

ReplyForm = model_form(Reply, base_class=FlaskForm, db_session=db.session)

@app.before_first_request
def initDB():
	db.create_all()

	reply = Reply(name="Matti", email="matti@mail.com")
	db.session.add(reply)

	reply = Reply(name="Maija", email="maija@mail.com")
	db.session.add(reply)

	reply = Reply(name="Maisa", email="maisa@mail.com")
	db.session.add(reply)

	db.session.commit() 

@app.route("/")
def replies():
	replies = Reply.query.all()
	return render_template("replies.html", replies=replies)

@app.route("/new", methods=["GET", "POST"])
def new():
	form = ReplyForm()

	if form.validate_on_submit(): 
		reply = Reply()
		form.populate_obj(reply)

		db.session.add(reply)
		db.session.commit()
	
		flash("Reply added.")
		return redirect("/")

		print("Reply added.")

	return render_template("new.html", form=form)

if __name__ == "__main__":
	app.run()
