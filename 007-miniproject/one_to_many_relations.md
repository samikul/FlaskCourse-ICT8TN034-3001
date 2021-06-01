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
