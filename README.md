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
* Kloonaa repositorio
* Käynnistä virtuaaliympäristö kansiossa jonne kloonasit repositorion
* hakemistossa tulee olla .env tiedosto, jossa on salainen avain SECRET_KEY=*************
* Tietokanta voidaan määrittää psql < schema.sql  komennolla
* muista vaihtaa oma tietokannan osoite kohtaan app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///cerfkris" app.py tiedostossa
* Sovellus avautuu kirjautumissivulle jossa voit myös rekisteröityä
* Luo käyttäjä ja kirjaudu sisään
* Käyttäjä voi lisätä blogeja palstalle ja tarkastella muiden julkaisuja 
