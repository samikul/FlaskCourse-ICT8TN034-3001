# Luento 28.5.2021 (Tero Karvinen)
### Hello Flask
- Hello Python!
- Hello Flask!
- Hello Jinja-templates!
- Validoi HTML
### Hello database
- Tuo `SQLAlchemy`
- Luo `SQLAlchemy`-luokan olio `db`
- Luo tietokanta luomalla X-luokka perimällä `db.Model`
- Määritä attribuutit luomalla `db.Column` luokan olioita
- Määritä tietokannan luonti `@app.before_first_request`
- Luo testidata luomalla X-luokan olioita
- Lisää transaktiot
- Luo muuttuja, johon lisätään tietokannan sisältö
- *R* Lähetä tietokannan sisältö muotille määrittämällä se `render_template` parametriksi
- Kirjoita muottiin `for`-silmukka, joka tulostaa tietokannan sisällön web-sivulle
### Hello automatic forms
- Tuo `FlaskForm`
- Tuo `model_form`
- Luo LomakeForm-luokka käyttämällä `model_form`-funktiota
- Luo uusi reitti, muotti ja testaa toimivuus
- Lisää sivulinkitykset `base.html`
- Luo reitille LomakeLuokan lomake-olio
- Luo sala-avain ja lisää se `app.secret_key ...`
- Luo muottiin silmukka, joka tulostaa lomakkeen
- Lisää `<form>` tagit silmukan ympärille ja lisää `POST` metodi
- Lisää `<submit>` painike
- Testaa, että pyyntö lähtee liikkeelle: selaimessa <kbd>F12</kbd> -> network -> pyyntö  -> request
- Piilota CSRF-kenttä

### Salasanatiivisteet
- `werkzeug` tarjoaa `generate_password_hash ja check_password_hash` 
```
$ generate_password_hash("salasana")
$ hashed_pass = generate_password_hash("salasana")
$ check_password_hash(hashed_pass, "salasana")
True
$ check_password_hash(hashed_pass, "pass")
False
```

