# Matematiikan tehtäväsovellus

Sovelluksessa ratkaistaan yksinkertaisia matemaattisia tehtäviä. Tällä hetkellä sovelluksessa on kaikki vaatimusmäärittelyn mainitsemat ominaisuudet graafista käyttöliittymää lukuunottamatta.  

Sovelluksen testien haarautumakattavuus on valitettavasti vielä alhainen, eikä arkkitehtuurikuvausta vielä ole.

##  Dokumentaatio

[Käyttöohje](https://github.com/ilrm123/ot-harjoitustyo/blob/master/dokumentaatio/kayttoohje.md)

[Vaatimusmäärittely](https://github.com/ilrm123/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)

[Työaikakirjanpito](https://github.com/ilrm123/ot-harjoitustyo/blob/master/dokumentaatio/tuntikirjanpito.md)

[Arkkitehtuurikuvaus](https://github.com/ilrm123/ot-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)

[Ensimmäinen release](https://github.com/ilrm123/ot-harjoitustyo/releases/tag/viikko5)

[Toinen release](https://github.com/ilrm123/ot-harjoitustyo/releases/tag/viikko6)

## Komentorivitoiminnot

Riippuvuudet asennetaan komennolla:

```bash
poetry install
```

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
