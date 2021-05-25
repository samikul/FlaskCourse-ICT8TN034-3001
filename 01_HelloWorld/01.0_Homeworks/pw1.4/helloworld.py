# Importoidaan flask kirjastosta luokka Flask.
from flask import Flask

# Luodaan Flask-luokan ilmentymä, jonka argumentiksi annetaan ohjelman moduuli.
# Moduulin nimi "__name__" tulee tiedostonimestä.
app = Flask("__name__")

# Määritetään URL-osoitteen pääte (endpoint),
@app.route("/")
# joka laukaisee määritetyn funktion,
def helloflask():
# joka palautaa merkkijonon.
	return "Hello Flask!\n"

# Ajaa ohjelman paikallisesti testiympäristössä. 
app.run()

