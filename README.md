# Matematiikan tehtäväsovellus

Sovelluksessa ratkaistaan yksinkertaisia matemaattisia tehtäviä. Lopullisessa sovelluksessa on kaikki vaatimusmäärittelyn mainitsemat ominaisuudet graafista käyttöliittymää lukuunottamatta.  

Sovelluksen testien haarautumakattavuus on valitettavasti alhainen, eikä arkkitehtuurikuvausta tai testausdokumenttia ole.

##  Dokumentaatio

[Käyttöohje](https://github.com/ilrm123/ot-harjoitustyo/blob/master/dokumentaatio/kayttoohje.md)

[Vaatimusmäärittely](https://github.com/ilrm123/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)

[Työaikakirjanpito](https://github.com/ilrm123/ot-harjoitustyo/blob/master/dokumentaatio/tuntikirjanpito.md)

~~Arkkitehtuurikuvaus~~ Ei ole

 ~~Testausdokumentti~~ Ei ole

[Ensimmäinen release](https://github.com/ilrm123/ot-harjoitustyo/releases/tag/viikko5)

[Toinen release](https://github.com/ilrm123/ot-harjoitustyo/releases/tag/viikko6)

[Lopullinen release](https://github.com/ilrm123/ot-harjoitustyo/releases/tag/viikko7)

## Komentorivitoiminnot

Riippuvuudet asennetaan komennolla:

```
poetry install
```

Ohjelma suoritetaan komennolla:

```
poetry run invoke start
```

Ohjelman testit suoritetaan komennolla:
```
poetry run invoke test
```

Ohjelman testikattavuusraportti generoidaan komennolla:
```
poetry run invoke coverage-report
```

Pylint-tarkistukset suoritetaan komennolla:
```
poetry run invoke lint
```
