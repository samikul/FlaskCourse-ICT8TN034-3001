## Luento 26.5

### Luennon 1. osio:

- asenna paketti
  - `python3-flask-sqlalchemy`
```python
if __name__ == "__main__":
	app.run
```

- Muotti laajentaa base.html
- Blokki, joka korvataan omalla datalla
  - `{% for thing in things %}` ...


## Esimerkkikoodi (Tero Karvinen, 26.5.2021)

```python
==> 
based.py
 <==
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy # sudo apt-get install flask_sqlaclhemy

app = Flask(__name__)
db = SQLAlchemy(app)

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String, nullable=False)
    name = db.Column(db.String, nullable=False)

@app.before_first_request
def initMe():
    db.create_all()

    comment = Comment(text="Great day!", name="Tero")
    db.session.add(comment)

    comment = Comment(text="Cloudy", name="Erkki Esimerkki")
    db.session.add(comment)

    db.session.commit()

@app.route("/")
def index():
    comments = Comment.query.all()
    return render_template("index.html", comments=comments)

if __name__ == "__main__":
    
app.run
()

==> templates/base.html <==
<!doctype html>
<html lang=en>
	<head>
		<title>Databases</title>
		<meta charset="utf-8">
	</head>
	<body>
		<h1>Databases</h1>
		{% block content%}
		{% endblock content%}
	</body>
</html>

==> templates/index.html <==
{% extends "base.html" %}

{% block content %}
	{% for comment in comments %}
		<p>{{ 
comment.name
 }}: {{ comment.text }}</p>
	{% endfor %}
{% endblock content %}
```
