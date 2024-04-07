# Blogipalsta_projekti

Sovelluksen avulla voi voi lukaista blogeja, joihin käyttäjät vivat regoida ja kommentoida.
Sovelluksen ominaisuuksia ovat:

* Käyttäjä voi kirjautua sisään ja ulos sekä luoda uuden tunnuksen.
* Käyttäjä näkee sovelluksen etusivulla listan blogipostauksista sekä jokaisen alueen reaktoiden ja viestien määrän ja viimeksi lähetetyn viestin ajankohdan.
* Käyttäjä voi reagoida julkaisuun peukulla tai alapeukulla.
* Käyttäjä voi kirjoittaa kommentin julkaisuun.
* Muut käyttäjät voivat reagoida ja vastata kommenteihin.
* Käyttäjä voi myös poistaa kommentinsa.
* Käyttäjä voi etsiä kaikki viestit, joiden osana on annettu sana.
* Ylläpitäjä voi lisätä ja poistaa viestejä.
* Ylläpitäjä voi julkaista lisää blogeja.

* Ohjeet testaajalle
* Tietokannassa tulee olla tämä taulu (CREATE TABLE users (id SERIAL PRIMARY KEY, username TEXT, password TEXT);
* hakemistossa tulee olla .env tiedostossa jossa on salainen avain SECRET_KEY=*************
* muista vaihtaa oma käyttäjä kohtaan app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///cerfkris" app.py tiedostossa
* Tällä hetkellä sovelluksessa toimii kirjautuminen ja virheviestit kirjautimesessa
