# Luento 31.5

### Tuotantopalvelimen käyttöönotto

##### Tulimuurin ja tietokannan käyttöönotto
```
sudo apt-get update
sudo apt-get install -y ufw
sudo ufw allow 22/tcp
sudo ufw enable
sudo apt-get install -y postgresql
sudo systemctl restart postgresql
sudo -u postgres createuser sami
sudo -u postgres createdb sami
sudo apt-get install -y python3-psycopg2
```
[PostgreSQL asennus](https://terokarvinen.com/2016/install-postgresql-on-ubuntu-new-user-and-database-in-3-commands/index.html) (Tero Karvinen, 2016)
#### PostgreSQL lisäys ohjelmaan
```
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql:///sami'
```
#### *
```python
if not User.query.filter_by(username="heiskane").first():
```
Hakee rekisteröidyt käyttäjät:
```sql
select * from public.user;
```
Hakee tietokantakäyttäjät:
```sql
select * from user;
```

## **
Käyttäjäluokassa email pitää olla uniikki
```python
unique=True
```
Tarkasta, ettei tietokannassa ole kyseistä kenttää
```python
if User.query.filter_by(email=user.email).first():
	flash("User already exits. Please log in!")
	return redirect("/login")
```
```python
class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	email = db.Column(db.String, nullable=False, unique=True)
	passwordHash = db.Column(db.String, nullable=False)
```
[FLASK SQLALCHEMY](https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/)
#### Apache
```
sudo apt-get install -y apache2
sudo systemctl start apache2

```
https://terokarvinen.com/2020/deploy-python-flask-to-production/?fromSearch=

Lukittu ryhmäkäyttäjä
```
# Luo projektikäyttäjä
sudo adduser samiwsgi
# 
sudo usermod --lock samiwsgi
# 
sudo mkdir public_wsgi
sudo chown samiwsgi:samiwsgi public_wsgi
sudo chmod d+rwxs public_wsgi
sudo adduser sami samiwsgi
exit
```
Shared, jaetut kansiot
https://terokarvinen.com//2011/shared-folder-with-chmod-setgid/index.html?fromSearch=

Teknisen käyttäjän luonti
```
sudo adduser samiwsgi
sudo usermod --lock samiwsgi

sudo mkdir /home/samiwsgi/public_wsgi/
sudo chown samiwsgi:samiwsgi /home/samiwsgi/public_wsgi/
sudo chmod g+rwxs /home/samiwsgi/public_wsgi/

sudo adduser sami samiwsgi
# todo: log out, log in
```
Sähköpostin lähetys:
- sendgrid tai mailgun
- python3-requests (requests)

https suojaus:
- letsencrypt
- lego
