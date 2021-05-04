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

Tämänhetkisessä sovelluksen versiossa on tekstikäyttöliittymä, ja valikko tulostuu komentoriville.

Valikossa on eri vaihtoehtoja, joista jokaisella on oma numero. Haluttu toiminto valitaan syöttämällä toiminnon vieressä oleva numero ja painamalla enteriä.
Ennen sisäänkirjautumista valikossa on vaihtoehdot:

1 - Kirjaudu sisään<br/>
2 - Luo uusi käyttäjä<br/>
0 - Sulje<br/>

Kirjautumisen jälkeen näkymä on:

1 - Kirjaudu ulos<br/>
2 - Luo uusi käyttäjä<br/>
3 - Yhteenlaskut<br/>
4 - Erotukset<br/>
5 - Kertolaskut<br/>
0 - Sulje<br/>

Toiminnot 3-5 ovat siis sovelluksen kolme tehtäväsarjaa, joissa on jokaisessa viisi satunnaisesti luotua melko helppoa laskua.
Kun tehtäväsarja on valittu, komentoriville ilmestyy jokin lauseke (esim. 24+83). Käyttäjän tulee seuraavaksi syöttää lausekkeen vastaus kokonaislukuna.
Vastaus tulkitaan vääräksi, jos se on väärin tai syöte on virheellinen (esim. merkkijono).
Kun vastaa kerralla kaikki viisi kysymystä oikein, niin valikossa näkyy että kyseinen tehtäväsarja on nyt suoritettu.
Kun kaikki tehtäväsarjat ovat suoritettu, niin on tehty kaikki mitä sovelluksessa voi tehdä.

