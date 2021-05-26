from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

from flask_wtf import FlaskForm
from wtforms.ext.sqlalchemy.orm import model_form

app = Flask(__name__)
app.secret_key = "uFuco0eiMueCheeth9dooQuahhie4ewihohm7iex"
db = SQLAlchemy(app)

class Comment(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String, nullable=False)
	text = db.Column(db.String, nullable=False)
	email = db.Column(db.String, nullable=False)

CommentForm = model_form(Comment, base_class=FlaskForm, db_session=db.session)

@app.before_first_request
def initMe():
	db.create_all()

	comment = Comment(name="Matti Meikäläinen", text="Tässäpä turha kommentti.", email="matti@mail.com")
	db.session.add(comment)

	comment = Comment(name="Maija Mansikka", text="No comments.", email="maija@posti.fi")
	db.session.add(comment)
	
	comment = Comment(name="Erkki Esimerkki", text="Bla bla bla!", email="erkki@mail.com")
	db.session.add(comment)

	db.session.commit()

@app.route("/newcomment", methods=["GET", "POST"])
def addForm():
	form = CommentForm()
	# print(request.form) # for tests
	return render_template("newcomment.html", form=form)

@app.route("/")
def index():
	comments = Comment.query.all()
	return render_template("index.html", comments=comments)

if __name__ == "__main__":
	app.run()
