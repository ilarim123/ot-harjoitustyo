# Matematiikan tehtäväsovellus

Sovelluksessa ratkaistaan yksinkertaisia matemaattisia tehtäviä. Tällä hetkellä sovelluksessa on mahdollista valita kolmesta tehtäväsarjasta yksi jonka tehtäviä ratkaisee. Sovelluksessa voi myös luoda uuden käyttäjän sekä kirjautua sisään ja kirjautua ulos, mutta sisäänkirjautuminen vaikuttaa toistaiseksi vain tulostettuun tekstiin eikä sillä ole mitään erikoista toiminnallisuutta. 

Sovelluksesta puuttuu vielä mahdollisuus kerätä käyttäjäkohtaisia pisteitä tehtävistä ja saada tehdyistä tehtäväsarjoista suoritusmerkintä. Tarkoituksena olisi myös luoda graafinen käyttöliittymä sekä mahdollisesti jotain muita toiminnallisuuksia. 

Sovelluksen testien haarautumakattavuus on vielä tämänhetkisiä vaatimuksia alhaisempi, ja arkkitehtuurikuvausta ei vielä ole.

##  Dokumentaatio

[Vaatimusmäärittely](https://github.com/ilrm123/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)

[Työaikakirjanpito](https://github.com/ilrm123/ot-harjoitustyo/blob/master/dokumentaatio/tuntikirjanpito.md)

[Arkkitehtuurikuvaus](https://github.com/ilrm123/ot-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)

## Komentorivitoiminnot

Ohjelma suoritetaan komennolla:

```bash
poetry run invoke start
```

Ohjelman testit suoritetaan komennolla:
```bash
poetry run invoke test
```

Ohjelman testikattavuusraportti generoidaan komennolla:
```bash
poetry run invoke coverage-report
```

Pylint-tarkistukset suoritetaan komennolla:
```bash
poetry run invoke lint
```
