from flask import Flask, render_template # sudo apt-get install -y python3-flask
from flask_sqlalchemy import SQLAlchemy # sudo apt-get install -y python3-flask-sqlalchemy

from flask_wtf import FlaskForm
from wtforms.ext.sqlalchemy.orm import model_form # sudo apt-get install -y python3-flaskext.wtf

app = Flask(__name__)
app.secret_key = "thoo4Noz1Aish4Gei2auraquaidow1"
db = SQLAlchemy(app)

class Message(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String, nullable=False)
	text = db.Column(db.String, nullable=False)
	email = db.Column(db.String, nullable=False)

MessageForm = model_form(Message, base_class=FlaskForm, db_session=db.session)

@app.before_first_request
def initDB():
	db.create_all()

	message = Message(name="Jaska Jokunen", text="Entten tentten teelikamentten.", email="jaska@mail.com")
	db.session.add(message)

	message = Message(name="Mikki Hiiri", text="Hissun kissun vaapula vissun.", email="mikki@mail.com")
	db.session.add(message)
	
	message = Message(name="Helinä Keiju", text="Eelin keelin klot.", email="helina@mail.com")
	db.session.add(message)

	message = Message(name="Nalle Puh", text="Viipula vaapula vot.", email="nalle@mail.com")
	db.session.add(message)

	db.session.commit()	

@app.route("/")
def index():
	messages = Message.query.all()
	return render_template("index.html", messages=messages)

@app.route("/contact", methods=["GET", "POST"])
def addForm():
	form = MessageForm()
	return render_template("contact.html", form=form)

if __name__ == "__main__":
	app.run()
