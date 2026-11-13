# Steam Games Data Analysis

Python nyelven készített adatelemző program, amely a Steam-játékok 2019-ben gyűjtött adatait vizsgálja. A program öt kérdésre válaszol, az eredményeket a terminálban írja ki, és grafikonokat készít.

## Felhasznált eszközök

- Python 3
- Pandas – adatok beolvasása, szűrése, csoportosítása
- NumPy – intervallumok középértéke, feltételes kategorizálás
- Matplotlib – grafikonok készítése

## Adatforrás

Nik Davis: [Steam Store Games (Clean dataset)](https://www.kaggle.com/datasets/nikdavis/steam-store-games), Kaggle. A Steam és a SteamSpy API-jából gyűjtött adatokat tartalmazza (2019. május). A `data/steam.csv` fájl 27 075 játék 18 adatmezőjét tartalmazza.

A felhasznált adathalmaz licence: [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/). Az adatfájlt változtatás nélkül használjuk, a belőle készült elemzések és grafikonok saját feldolgozások.

## Elemzési kérdések és módszerek

1. **Mely műfajokból szerepel a legtöbb játék az adatbázisban?** A `genres` oszlop felbontása és a tíz leggyakoribb műfaj megszámlálása. A játékok több műfajhoz is tartozhatnak.
2. **Mekkora a fizetős játékok átlagára a leggyakoribb műfajokban?** Csak a 0 GBP-nél drágább játékok szerepelnek a vizsgálatban. A tíz legtöbb fizetős játékot tartalmazó műfaj átlagát és mediánját számítjuk ki.
3. **Hogyan változott a megjelent játékok száma évenként?** A `release_date` oszlopból évszámokat nyerünk ki. A grafikon 2018-ig tart, mert az adathalmazban 2019 csak részleges év.
4. **Mekkora a becsült tulajdonosszám az ingyenes és a fizetős játékok esetén?** Az `owners` oszlop tartományainak középértékével becslünk, majd a két csoport átlagát és mediánját számítjuk. A középérték nem pontos tulajdonosszám.
5. **Van-e kapcsolat a játék ára és a pozitív értékelések aránya között?** A pozitív arányt a pozitív értékelések és az összes értékelés hányadosából számítjuk. Csak legalább 20 értékeléssel rendelkező, legfeljebb 50 GBP-s fizetős játékokat vizsgálunk, Pearson-korrelációval.

## Néhány eredmény

- A leggyakoribb műfaj az **Indie** (19 421 előfordulás).
- 2018-ban 8 160 játék szerepel az adathalmaz megjelenési statisztikájában.
- Az ingyenes játékok becsült tulajdonosszámának mediánja 35 000, a fizetős játékoké 10 000.
- Az ár és a pozitív értékelési arány Pearson-korrelációja a szűrt mintán körülbelül **0,115**, azaz gyenge pozitív lineáris kapcsolat.

Az eredmények az adathalmazban szereplő játékokra érvényesek, és nem tükrözik a Steam aktuális kínálatát. A kapcsolat nem jelent ok-okozati összefüggést.

## Telepítés és futtatás

A projekt mappájában:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python main.py
```

A menüben az 1–5 számokkal indíthatók az elemzések, a `0` kilép. A grafikonok automatikusan a `charts/` mappába kerülnek PNG-formátumban.

## Fájlok

- `main.py` – programindítás és menürendszer
- `analysis.py` – adatfeldolgozás és az öt elemzés
- `requirements.txt` – szükséges könyvtárak
- `data/steam.csv` – felhasznált adatok
- `charts/` – a program által készített grafikonok
