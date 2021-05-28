# Luento 28.5.2021
[Tero Karvinen](https://terokarvinen.com)
## FLASK CRUD
Web-appin luonti pienin mahdollinen testattava osa kerrallaan
### Hello Flask
- Hello Python!
- Hello Flask!
- Hello Jinja-templates!
- Validoi HTML
### Hello Database
- Tuo `SQLAlchemy`
- Luo `SQLAlchemy`-luokan olio `db`
- Luo tietokanta luomalla X-luokka perimällä `db.Model`
- Määritä attribuutit luomalla `db.Column` luokan olioita
- Määritä tietokannan luonti `@app.before_first_request`
- Luo testidata luomalla X-luokan olioita
- Lisää transaktiot
### Hello Read
- Luo muuttuja, johon lisätään tietokannan sisältö
- Lähetä tietokannan sisältö muotille määrittämällä se `render_template` parametriksi
- Kirjoita muottiin `for`-silmukka, joka tulostaa tietokannan sisällön web-sivulle
### Hello Automatic Forms
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
### Hello Create
- Lisää add-reitin parametrin `methods` arvoiksi `GET` ja `POST`
- Lisää add-reitin funktioon datan palvelinpuolen validointia ehtolausekkeella
- Luo tyhjä X-luokan olio
- Lisää lomakkeen data populoimalla se x-olioon
- Lisää `print()` debuggaus
- Lisää data tietokantaan
- Kokeile toimivuus selaimella
### Hello Flash Messages
- Tuo `flash` ja `redirect`
- Lisää em. reitin funktioon `flash("Viesti")` ja uudelleenreititys `redirect("/")`
- Lisää tiedostoon `base.html` silmukka flash-viesteille
### Hello Update
- Lisää muottiin edit-linkki, jonka URL:iin lisätään kyseisen kentän id ja `/edit` endpoint
- Lisää reitti, joka käsittelee URL:in mukana tulevan id:n
- Lisää käsittelevään funktioon arvo id=None
- Lisää ehto: if id=True
- ... *JATKA TÄSTÄ*
### Hello Delete
- Lisää muottiin delete-linkki, jonka URL:iin lisätään kyseisen kentän id ja `/delete` endpoint
- Luo uusi reitti poistolle
- Luo funktio ja anna sen parametriksi `id`
- luo X-luokan oliosta muuttuja, joka palauttaa 404-virheilmoituksen, jos käyttäjä lähettää vääriä url-kutsuja
- Lisää tietokantakäsittely
- Lisää transaktion
- Lisää uudelleenohaus
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

