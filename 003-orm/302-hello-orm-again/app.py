################
## TO BE FIXED # 
################
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)

class Reply(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String, nullable=False)
	email = db.Column(db.String, nullable=False)
	need_a_ride = db.Column(db.Boolean, nullable=False)
	extra_info = db.Column(db.String, nullable=True)

@app.before_first_request
def initMe():
	db.create_all()

	reply = Reply(name="Matti Meikäläinen", email="matti@email.com", need_a_ride=True, extra_info="Etupenkkipaikka kiitos")
	db.session.add(reply)

        reply = Reply(name="Erkki Esimerkki", email="erkki@email.fi", need_a_ride=False, extra_info="Tuun taksilla")
        db.session.add(reply)

        reply = Reply(name="Maija Meikäläinen", email="maija@email.fi", need_a_ride=True, extra_info="Myöhässä 10min")
        db.session.add(reply)

	db.session.commit()
	

@app.route("/")
def index():
	replies = Reply.query.all()
	return render_template('index.html', title='Replies' replies=replies)

if __name__ == "__main__":
	app.run()
