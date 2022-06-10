"""
3 csoportba soroljuk az adatokat:

1. structured  - strukturált adatok -> relációs adatbázisnól érkezik
2. semi structured - CSV, XML, JSON, parquet
3. unstructed data - struktúrálatlan adat ->  videó, kép, hang

ETL - Extract Transform Load  - adat integrációt

OLAP - analitikus - Adattárháznak (Data Warehouse, Data Lake, Data Lakehouse)
OLTP - Online tranzakciós adatbázis - a mi feladatunk az OLTP

--------------------------------------------------------------------------
(adatbázis közeli fejlesztők)
1. Átmeneti táblába érkeztetjük az adatot, módosulatlan - nagyon minimálos módosítás 
    (Data Enrichment - adat dúsítás)
   Aztán tovább töltjük az adatot a végleges helyére: 
    - adattisztítás
    - tipusosítás
    - adatmodell kialkításnak megfelelően az adat csoportosítása

2. Egyből a végtábla fogjuk tölteni az adatot, minden módosítás elvégzése után

3. Magát a file-t használjuk úgy, mint egy tábla -> felhőzünk


"""

"""
create table meta_data (
adult bool,
backdrop_path text,
original_language text,
original_title text,
overview text,
popularity numeric,
poster_path text,
release_date text,
title text,
video bool,
vote_average numeric,
vote_count int
)
"""