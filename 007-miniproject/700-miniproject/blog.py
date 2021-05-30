from flask import Flask, render_template, redirect, flash # sudo apt-get install -y python3-flask
from flask_sqlalchemy import SQLAlchemy # sudo apt-get install -y python3-flask-sqlalchemy

from flask_wtf import FlaskForm
from wtforms.ext.sqlalchemy.orm import model_form # sudo apt-get install -y python3-flaskext.wtf

app = Flask(__name__)
app.secret_key = "joleeficaeghisdfgeR9exohzuioph678eitohquei2"
db = SQLAlchemy(app)

class Post(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	author = db.Column(db.String, nullable=False)
	heading = db.Column(db.String, nullable=False)
	text = db.Column(db.Text, nullable=False)

PostForm = model_form(Post, base_class=FlaskForm, db_session=db.session)

@app.before_first_request
def initDB():
	db.create_all()

	post = Post(author="Matti Meikäläinen", heading="Ensimmäinen postaus",
	text="Lorem ipsum dolor sit amet, consectetur adipiscing elit.")
	db.session.add(post)

	post = Post(author="Matti Meikäläinen", heading="Toinen postaus",
	text="Curabitur vitae convallis mauris, vitae ornare ligula.")
	db.session.add(post)

	post = Post(author="Matti Meikäläinen", heading="Kolmas postaus",
	text="Integer in blandit quam, ut feugiat augue.")
	db.session.add(post)

	db.session.commit()

@app.route("/")
def homeView():
	return render_template("index.html")

@app.route("/blog")
def blogView():
	posts = Post.query.all()
	return render_template("blog.html", posts=posts)

@app.route("/<int:id>/edit", methods=["GET", "POST"])
@app.route("/newpost", methods=["GET", "POST"])
def createPost(id=None):
	post = Post()
	if id:
		post = Post.query.get_or_404(id)

	form = PostForm(obj=post)

	if form.validate_on_submit():
		form.populate_obj(post)

		db.session.add(post)
		db.session.commit()

		flash("Post added")
		return redirect("/blog")

		# print("Post added") # test only

	return render_template("newpost.html", form=form)

@app.route("/<int:id>/delete")
def deletePost(id):
	post = Post.query.get_or_404(id)
	db.session.delete(post)
	db.session.commit()

	flash("Post deleted.")
	return redirect("/blog")

if __name__ == "__main__":
	app.run()
