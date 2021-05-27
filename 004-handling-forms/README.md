# Luento 27.5.
CR-appin luonti vaihe vaiheelta
### Python3, Flask, Jinja
1. Luo Python-helloworld
2. Luo Flask-helloworld
3. Luo Jinja-muotit
4. Validoi HTML
5. Halutessa `title` muttujaan templaten ylälaitaan
### Tietokannan automaattinen luonti
1. Tuo SQLAlchemy
2. Luo SQLAlchemy luokan `db`-olio
3. Luo luokka (joka samalla nimeää taulun)
4. Luo funktio, joka tekee tietokannan
5. Luo testitietueet em. funktion sisään
6. Aseta testidata muuttujaan ja aseta se `render_template()` funktion parametriksi
7. Kirjoita muottiin silmukka, joka tulostaa tietokannan
### Automaattilomakkeiden luonti
1. Tuo FlaskForm
2. Tuo model_form
3. Luo lomakeolio
4. Luo `base.html` muottiin linkit
5. Luo lomakeluokan olio
5. Aseta olio `render_template()` funktion parametriksi
6. Luo lomakemuotti
7. Luo ja lisää CSRF sala-avain
8. Kirjoita muottiin silmukka, joka tulostaa lomakkeen
9. Lisää lomakkeeseen POST-metodi
10. Piilota CSRF-label if-ehtolauseella
11. Lisää `submit` painike
### Lomakedatan lähetys
1. Luo funktio, joka validoi lomakkeelta tulevan datan
2. Luo luokan olio
3. Populoi tietokannan objektit
4. Lisää uusi olio tietokantaan
## Em. liittyviä muistiinpanoja
*Muotit ajetaan palvelimella, joten hakukoneet löytävät Jinja-muttujiin asetetun tiedon*
```jinja
<!-- base.html -->
{% if not title %}
        {% set title = "foo" %}
{% endif %}
```
```jinja
<!-- index.html -->
{% set title = "bar" %}
```
```
$ sudo apt-cache search hakusana1 hakusana2
```
Onelineri CSRF-kentän piilottamiseen
```
{{ field.label if not field.flags.hidden }}
```
```
$ sudo apt-get install -y pwgen
$ pwgen 30 1
```
## Teron esimerkkikoodit (Tero Karvinen, 27.5.2021)
#### iveseen.py
```python
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm # m
from wtforms.ext.sqlalchemy.orm import model_form # m

app = Flask(__name__)
app.secret_key = "CohlahT9chiel0onibae4eesee9zee"
db = SQLAlchemy(app)

class Animal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

AnimalForm = model_form(Animal, base_class=FlaskForm, db_session=db.session)

@app.before_first_request
def initDb():
    db.create_all()

    animal = Animal(name="Mallard")
    db.session.add(animal)

    animal = Animal(name="Jackdaw")
    db.session.add(animal)

    db.session.commit()

@app.route("/new", methods=["GET", "POST"])
def newAnimal():
    form = AnimalForm()

    if form.validate_on_submit():
        animal = Animal()
        form.populate_obj(animal)
        
        db.session.add(animal)
        db.session.commit()
        
        print("Added your animal, thanks.")
        # flash("Added")
        # redirect("/")

    return render_template("new.html", form=form)

@app.route("/")
def index():
    animals = Animal.query.all()
    return render_template("index.html", animals=animals)

if __name__ == "__main__":
    
app.run()
```
#### templates/base.html
```html
{% if not title %}
{% set title="Iveseen - the animalistic app" %}
{% endif %}

<!doctype html>
<html lang=en>
	<head>
		<title>{{ title }}</title>
		<meta charset="utf-8">
		<meta name=viewport content="width=device-width, initial-scale=1">
	</head>
	<body>
		<nav>
			<a href="/">Home</a> - 
			<a href="/new">New</a>
		</nav>
		<h1>{{ title }}</h1>
		{% block content %}
		<p>Hello, world!</p>
		{% endblock content %}
	</body>
</html>
```
#### templates/index.html
```html
{% set title="Animal base" %}
{% extends "base.html" %}

{% block content %}

{% for animal in animals %}
<p>{{ 
animal.name
 }}</p>
{% endfor %}


{% endblock content %}
```
#### templates/new.html
```html
{% set title="Add new animal you've seen" %}
{% extends "base.html" %}

{% block content %}

<form method=POST>
{% for field in form %}
	<p>
		{% if not field.flags.hidden %}
			{{ field.label }}<br> 
		{% endif %}
		
		{{ field }}
	</p>
{% endfor %}
	<input type=submit>
</form>

{% endblock content %}
```
## Update
1. Lisää uusi reitti, johon sijoitetaan rajoitettu muuttujan tyyppi `/<int:id>/edit`
...
## Teron esimerkkikoodi UPDATE-ominaisuudesta (Tero Karvinen, 27.5.2021)
```python 
# iveseen.py

from flask import Flask, render_template, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm # m
from wtforms.ext.sqlalchemy.orm import model_form # m

app = Flask(__name__)
app.secret_key = "CohlahT9chiel0onibae4eesee9zee"
db = SQLAlchemy(app)

class Animal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)

AnimalForm = model_form(Animal, base_class=FlaskForm, db_session=db.session)

@app.before_first_request
def initDb():
    db.create_all()

    animal = Animal(name="Mallard")
    db.session.add(animal)

    animal = Animal(name="Jackdaw")
    db.session.add(animal)

    db.session.commit()

@app.route("/<int:id>/edit", methods=["GET", "POST"])
@app.route("/new", methods=["GET", "POST"])
def newAnimal(id=None):
    animal = Animal()
    if id:
        animal = Animal.query.get_or_404(id)

    form = AnimalForm(obj=animal)

    if form.validate_on_submit():
        form.populate_obj(animal)
        
        db.session.add(animal)
        db.session.commit()
        
        flash("Added")
        return redirect("/")

    return render_template("new.html", form=form)

@app.route("/")
def index():
    animals = Animal.query.all()
    return render_template("index.html", animals=animals)

if __name__ == "__main__":
    
app.run
()
```
```html
==> templates/base.html <==
{% if not title %}
{% set title="Iveseen - the animalistic app" %}
{% endif %}

<!doctype html>
<html lang=en>
	<head>
		<title>{{ title }}</title>
		<meta charset="utf-8">
		<meta name=viewport content="width=device-width, initial-scale=1">
	</head>
	<body>
		<nav>
			<a href="/">Home</a> - 
			<a href="/new">New</a>
		</nav>

		{% for msg in get_flashed_messages() %}
			<p><b>{{ msg }}</b></p>
		{% endfor %}		

		<h1>{{ title }}</h1>
		{% block content %}
		<p>Hello, world!</p>
		{% endblock content %}
	</body>
</html>
```
```html
==> templates/index.html <==
{% set title="Animal base" %}
{% extends "base.html" %}

{% block content %}

{% for animal in animals %}
	<p>
		{{ 
animal.name
 }} - 
		<a href="{{ 
animal.id
 }}/edit">Edit</a>
	</p>
{% endfor %}


{% endblock content %}
```
```html
==> templates/new.html <==
{% set title="Add new animal you've seen" %}
{% extends "base.html" %}

{% block content %}

<form method=POST>
{% for field in form %}
	<p>
		{% if not field.flags.hidden %}
			{{ field.label }}<br> 
		{% endif %}
		
		{{ field }}
	</p>
{% endfor %}
	<input type=submit>
</form>

{% endblock content %}
```
## DELETE
1. Lisää templateen Delete-linkki
2. Vaihda endpointin loppu `/delete`
3. Lisää reitti ym. endpointiin
4. Luo DELETE-funktio ja anna sille parametriksi ID
5. Luo uusi X luokan olio, joka haetaan ID:n perusteella tai antaa 404-virheilmoituksen
6. Lisää poisto tietokannasta
7. Lisää transaktio
8. Lisää flash-message
9. Lisää poiston jälkeinen uudelleenohjaus
### Teron esimerkkikoodi (Tero Karvinen, 27.5.2021)
```python
@app.route("/<int:id>/delete")
def deleteAnimal(id):
    animal = Animal.query.get_or_404(id)
    db.session.delete(animal)
    db.session.commit()

    flash("Deleted.")
    return redirect("/")
```
