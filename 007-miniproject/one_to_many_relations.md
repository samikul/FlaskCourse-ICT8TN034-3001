# One-to-many-relations
[Flask-SQLAlchemy documentation](https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/).

```
### Many-luokkaan:
...
category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
category = db.relationship('Category', backref=db.backref('posts', lazy=True))
...
... editTask():
...
task.user = User.query.get(session["uid"])
...
```
### Rajoitukset
```python
def userLevelRequided(level):
	user = User.query.get(session["uid"])
	if not user.level>=100:
		abort(403)

...
userLevelRequired(100)
...
```
```
# relationships
#       user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
#       user = db.relationship("User", backref=db.backref("Contacts", lazy=True))
```
```
category_id = db.Column(db.Integer, db.ForeignKey('
category.id
'),
        nullable=False)
    category = db.relationship('Category',
        backref=db.backref('posts', lazy=True))
```
```
@app.route("/task/edit/<int:id>",  methods=["GET", "POST"])
@loginRequired
def editTask(id=None):
	if id:
		task = Task.query.get(id)
		if task.user.id
			!= session["uid"]:
			return redirect("/user/login")
	else:
		task = Task()
```
```
from x import * # only fow my own code
```
