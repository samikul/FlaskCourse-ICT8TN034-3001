# Luento 26.5

## Luennon 1. osio:

- asenna paketti
  - `python3-flask-sqlalchemy`
```python
if __name__ == "__main__":
	app.run
```

- Muotti laajentaa base.html
- Blokki, joka korvataan omalla datalla
  - `{% for thing in things %}` ...


### Esimerkkikoodit (Tero Karvinen, 26.5.2021)

#### Hello ORM!

##### based.py
```python
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy # sudo apt-get install flask_sqlalchemy

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
```
##### templates/base.html
```html
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
```
##### templates/index.html
```html
{% extends "base.html" %}

{% block content %}
	{% for comment in comments %}
		<p>{{ comment.name }}: {{ comment.text }}</p>
	{% endfor %}
{% endblock content %}
```

- ORM säästää aikaa, vaivaa ja kirjoittamista
  - Luokka voi tehdä myös lomakkeen ja hoitaa validointia
- Tietokantojen kanssa tulee käyttää frameworkeja 
  - Antaa tietoturvaa ja suojaa mm. injektioilta
    - Nyt käytössä Jinja ja SQLAlchemy


## Luennon 2. osio

- haku paketinhallinnasta
  - `apt-cache search hakusana1 hakusana2`
- `sudo apt-get install -y python3-flaskext.wtf`
- [Flask Automatic Forms](https://terokarvinen.com/2020/flask-automatic-forms/)

- model_form ja FlaskForm
- Luokasta tehdään lomakeluokka
- parametrina on aina FlaskForm(db.session)
- metodeissa pitää luetella myös post
- `sudo apt-get install -y pwgen`
  - `pwgen 30 1`

```
{% if not field.flags.hidden %}
```

- Micro:
  - `ctrl-E set softwrap on`

- placeholder
  - https://betterprogramming.pub/how-to-use-flask-wtforms-faab71d5a034
  - https://github.com/heiskane/python_flask_homework/blob/main/day3/products/templates/add_product.html

### Esimerkkikoodit (Tero Karvinen, 26.5.2021)

#### Hello automatic forms!

##### based.py
```python
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy # sudo apt-get install python3-flask-sqlaclhemy

from flask_wtf import FlaskForm
from wtforms.ext.sqlalchemy.orm import model_form

app = Flask(__name__)
app.secret_key = "eeth.iethoongavot1Oqu9ri2ien8s"
db = SQLAlchemy(app)

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String, nullable=False)
    name = db.Column(db.String, nullable=False)
    feeling = db.Column(db.String)

CommentForm = model_form(Comment, 
    base_class=FlaskForm, db_session=db.session)

@app.before_first_request
def initMe():
    db.create_all()

    comment = Comment(text="Great day!", name="Tero")
    db.session.add(comment)

    comment = Comment(text="Cloudy", name="Erkki Esimerkki")
    db.session.add(comment)

    db.session.commit()

@app.route("/new", methods=["GET", "POST"])
def addForm():
    form = CommentForm()
    print(request.form) # test only
    return render_template("new.html", form=form)

@app.route("/")
def index():
    comments = Comment.query.all()
    return render_template("index.html", comments=comments)

if __name__ == "__main__":
    
app.run()
```
##### templates/new.html
```html
{% extends "base.html" %}

{% block content %}
	<p>New commment</p>

	<form method=POST>
		{% for field in form %}
		<p>{{ field.label }}: {{ field }}</p>
		{% endfor %}
		<input type=submit>
	</form>
{% endblock content %}
```

### Redirect ja flashed messages
##### .py
```python
... import redirect
...
@app.route("/msg")
def msgPage():
    flash("Here is a message for you!")
    return redirect("/")
```
##### .html
```html
{% if get_flashed_messages() %}                                         
                        {% for message in get_flashed_messages() %}                     
                                <p><b>{{ message }}</b></p>                             
                        {% endfor %}
                {% endif %}
```

- https://flask.palletsprojects.com/en/1.0.x/quickstart/#message-flashing
- https://flask.palletsprojects.com/en/1.0.x/patterns/flashing/#message-flashing-pattern

### Kertaus

#### rakenna flaskrunko
Miten rakennetaan aiempi sovellus:
1. testaa python3 toimivuus
2. testaa flaskin toimivuus `# sudo apt-get install -y python3-flask`
3. tee helloflask
4. testaa reititys
5. luo muotit
6. validoi HTML
7. testaa toimivuus
#### lisää tietokanta
1. lisää sqlalchemy `# sudo apt-get install -y python3-flask-sqlalchemy`
2. anna sqlalchemyn luoda tietokanta `db = SQLAlchemy(app)` 
3. luo tietokantaluokka ja kentät määrityksineen. tämä luokka luo tietokannan ja myöhemmin myös lomakkeen
4. käynnistä ohjelma ja debuggaa kirjoitusvirheet
5. luo funktio, joka luo tietokannan `@app.before_first_request ...`
6. lisää esimerkkitietueet/testidata: `db.Column(db.Text,...)` on pitkälle tekstille
7. käynnistä ohjelma ja debuggaa typot
8. tulosta testitietueet sivulle `Comment.query.all() ...`
9. lisää `{% for silmukka %}` joka tulostaa testidatan
10. testaa toimivuus
#### lisää automaattiset lomakkeet
1. tuo `flask_wtf from FlaskForm` `# sudo apt-get install -y python3-flaskext.wtf`
2. tuo `model_form`
3. luo lomakkeen luova määritys `model_form`:lla
4. luo uusi muotti lomakkeelle
5. lisää `base.html` nav-linkitys uusille sivulle helpottaakseen työtä
6. lisää taulukko parametriksi, jotta se voidaan renderöidä
7. tee muottiin silmukka, joka luo lomakkeen
8. debuggaa virheet
9. luo secret key `pwgen 30 1`
10. testaa toimivuus
11. lisää muottiin `<form...` ja submit-nappula
12. lisää ehto, jolla piilotetaan CRSF-token
13. testaa toimivuus ja POST-metodin toimivuus

#### Esimerkkikoodi ylläolevasta (Tero Karvinen, 26.5.2021)
```python
==> 
guestbook.py
 <==
from flask import Flask, render_template # sudo apt-get install python3-flask
from flask_sqlalchemy import SQLAlchemy # sudo apt-get install python3-flask-sqlalchemy

from flask_wtf import FlaskForm # sudo apt-get install 
python3-flaskext.wtf

from wtforms.ext.sqlalchemy.orm import model_form


app = Flask(__name__)
app.secret_key = 'ahcoh7voo4iohae(fe1Ainoow6ainaeh#ei]ti'
db = SQLAlchemy(app)

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    text = db.Column(db.Text, nullable=False)    

CommentForm = model_form(Comment, base_class=FlaskForm, db_session=db.session)

@app.before_first_request
def initDb():
    db.create_all()

    comment = Comment(name="SuperNinja", text="I was here")
    db.session.add(comment)
    db.session.commit()

@app.route("/new")
def newComment():
    form = CommentForm()
    return render_template("new.html", form=form)

@app.route("/")
def index():
    comments = Comment.query.all()
    return render_template("index.html", comments=comments)

if __name__ == "__main__":
    
app.run
()
´´´
´´´html
==> templates/base.html <==

{% if not title %}
	{% set title="Tero's New Guestbook" %}
{% endif %}

<!doctype html>
<html lang=en>
	<head>
		<title>{{ title }}</title>
		<meta charset="utf-8">
	</head>
	<body>
		<nav>
			<a href="/">Home</a> - 
			<a href="/new">New</a>
		</nav>
		<h1>{{ title }}</h1>

		{% block content %}
		<p>Welcome!</p>
		{% endblock content %}
	</body>
</html>
```
```html
==> templates/index.html <==
{% set title="Karvinen's Guestbook" %}

{% extends "base.html" %}

{% block content %}
<p>This is the front page</p>

{% for comment in comments %}
<p>{{ comment.name }}: {{ comment.text }}</p>
{% endfor %}

{% endblock content %}
```
```html
==> templates/new.html <==
{% set title="Add new comment" %}

{% extends "base.html" %}

{% block content %}

<p>Thanks already.</p>

<form method=POST>
{% for field in form %}
<p>
{% if not field.flags.hidden %}
	{{ field.label }}
{% endif %} 
{{ field }}
</p>
{% endfor %}
<input type=submit>
</form>

{% endblock content %}
```
