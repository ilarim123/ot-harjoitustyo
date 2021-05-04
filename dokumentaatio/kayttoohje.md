# Käyttöohje

## Ohjelman käynnistäminen

Asenna riippuvuudet ennen ohjelman käynnistämistä komennolla:

```bash
poetry install
```

Sitten ohjelman voi käynnistää komennolla:

```
poetry run invoke start
```

## Valikon käyttäminen

Tämänhetkisessä sovelluksen versiossa on tekstikäyttöliittymä, ja valikko tulostuu terminaaliin.

Valikossa on eri vaihtoehtoja, joista jokaisella on oma numero. Haluttu toiminto valitaan syöttämällä toiminnon vieressä oleva numero ja painamalla enteriä.
Ennen sisäänkirjautumista valikossa on vaihtoehdot:

1 - Kirjaudu sisään
2 - Luo uusi käyttäjä
0 - Sulje

Kirjautumisen jälkeen näkymä on:

1 - Kirjaudu ulos
2 - Luo uusi käyttäjä
3 - Yhteenlaskut
4 - Erotukset
5 - Kertolaskut
0 - Sulje

Toiminnot 3-5 ovat siis sovelluksen kolme tehtäväsarjaa, joissa on jokaisessa viisi satunnaisesti luotua melko helppoa laskua.
Kun tehtäväsarja on valittu, terminaaliin ilmestyy jokin lauseke (esim. 24+83). Käyttäjän tulee seuraavaksi syöttää lausekkeen vastaus kokonaislukuna.
Vastaus tulkitaan vääräksi, jos se on väärin tai syöte on virheellinen (esim. merkkijono).
Kun vastaa kerralla kaikki viisi kysymystä oikein, niin valikossa näkyy että kyseinen tehtäväsarja on nyt suoritettu.
Kun kaikki tehtäväsarjat ovat suoritettu, niin on tehty kaikki mitä sovelluksessa voi tehdä.

