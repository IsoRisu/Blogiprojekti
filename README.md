# Blogipalsta_projekti

* Ohjeet testaajalle
* Kloonaa repositorio

* Suorita seuraavat komennot Blogiprojekti kansiossa
* python3 -m venv venv
* source venv/bin/activate
* pip install -r ./requirements.txt
* psql < schema.sql
* hakemistossa tulee olla .env tiedosto, jossa on salainen avain SECRET_KEY= ja DATABASE_URL=
* flask run

* Sovellus avautuu kirjautumissivulle jossa voit myös rekisteröityä
* Luo käyttäjä ja kirjaudu sisään
* Käyttäjä voi lisätä blogeja palstalle ja tarkastella muiden julkaisuja
* Blogeja voi arvostella ja kommentoida
* Käyttäjä voi kirjautua ulos
* Käyttäjän voi korottaa ylläpitäjäksi tietokannassa komennolla 
> psql 
# INSERT INTO admins (user_id) VALUES (KÄYTTÄJÄN ID NUMERO TÄHÄN);
* Ylläpijänä voi poistaa kommenteja ja blogipostauksia
