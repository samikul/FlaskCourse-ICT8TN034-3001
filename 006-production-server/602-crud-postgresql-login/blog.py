from flask import Flask, render_template, redirect, flash, session # sudo apt-get install -y python3-flask
from flask_sqlalchemy import SQLAlchemy # sudo apt-get install -y python3-flask-sqlalchemy

from flask_wtf import FlaskForm
from wtforms.ext.sqlalchemy.orm import model_form # sudo apt-get install -y python3-flaskext.wtf

from werkzeug.security import generate_password_hash, check_password_hash
from wtforms import StringField, PasswordField, validators

app = Flask(__name__)
app.secret_key = "joleeficaeghisdfgeR9exohzuioph678eitohquei2"
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql:///sami'
db = SQLAlchemy(app)

class Post(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	author = db.Column(db.String, nullable=False)
	heading = db.Column(db.String, nullable=False)
	text = db.Column(db.Text, nullable=False)

PostForm = model_form(Post, base_class=FlaskForm, db_session=db.session)

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	email = db.Column(db.String, nullable=False, unique=True)
	passwordHash = db.Column(db.String, nullable=False)

	def setPassword(self, password):
		self.passwordHash = generate_password_hash(password)

	def checkPassword(self, password):
		return check_password_hash(self.passwordHash, password)

class UserForm(FlaskForm):
	email = StringField("email", validators=[validators.Email()])
	password = PasswordField("password", validators=[validators.InputRequired()])

@app.before_first_request
def initDB():
	db.create_all()

	db.session.commit()

@app.errorhandler(404)
def custom404(e):
	return render_template("404.html")

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
	loginRequired()
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
	loginRequired()
	post = Post.query.get_or_404(id)
	db.session.delete(post)
	db.session.commit()

	flash("Post deleted.")
	return redirect("/blog")

########
# USER #
########

def loginRequired():
	if not currentUser():
		abort(403)

def currentUser():
	try:
		uid = int(session["uid"])
	except:
		return None
	return User.query.get(uid)

app.jinja_env.globals["currentUser"] = currentUser

@app.route("/user/register", methods=["GET", "POST"])
def signupView():
	form = UserForm()

	if form.validate_on_submit():
		email = form.email.data

		password = form.password.data

		if User.query.filter_by(email=email).first():
			flash("This user already exists. Please sign in.")
			return redirect("/user/login")

		user = User(email=email)
		user.setPassword(password)

		db.session.add(user)
		db.session.commit()

		flash("You have successfully signed up!")
		return redirect("/user/login")

	return render_template("signup.html", form=form)

@app.route("/user/login", methods=["GET", "POST"])
def loginView():
	form = UserForm()

	if form.validate_on_submit():
		email = form.email.data

		password = form.password.data

		user = User.query.filter_by(email=email).first()
		if not user:
			flash("Login failed.")
			print("No such user") # test only
			return redirect("/user/login")
		if not user.checkPassword(password):
			flash("Login failed.")
			print("Wrong password") # test only
			return redirect("/user/login")

		session["uid"]=user.id

		flash("Login successful.")
		return redirect("/")

	return render_template("login.html", form=form)

@app.route("/user/logout")
def logoutView():
	session["uid"] = None
	flash("Logged out successfully.")
	return redirect("/")

if __name__ == "__main__":
	app.run()
