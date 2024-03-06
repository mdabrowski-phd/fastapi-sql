"""ZADANIA"""

import numpy as np
import pandas as pd
import psycopg2

"""ZADANIE 1
Wczytaj dane z pliku cars.csv i wyodrębnij z niego kolumny: (price, brand, fuel, power, prod_year)
Następnie napisz zapytanie CREATE, które utworzy tabelę o takim samym schemacie + dodatkowa kolumna id typu serial.
Wykonaj zapytanie za pomocą psycopg2.
"""

conn = psycopg2.connect(dbname="postgres", user="postgres", password="postgres", host='localhost')
cursor = conn.cursor()

df = pd.read_csv("cars.csv", usecols=["price", "brand", "fuel", "power", "prod_year"]).iloc[:10]
print(df.head())

create_query = """CREATE TABLE cars(
    id SERIAL,
    price INTEGER,
    brand TEXT,
    fuel TEXT,
    power SMALLINT,
    prod_year SMALLINT
)
"""

# cursor.execute(create_query)
# conn.commit()

"""ZADANIE 2
Napisz kod, który na podstawie numeru indeksu wiersza dataframe'a, wyciągnie ten wiersz z tabeli,
utworzy zapytanie INSERT a następnie wykona je na bazie.
Podpowiedź:
Poniższy kod zamieni typy danych w rekordzie z df-a z numpyowych na zwykłe. Będzie to przydatne podczas insertowania.
[x.item() if isinstance(x, np.generic) else x for x in record.values]
"""


def get_row_from_df(df_, idx):
    return df_.loc[idx]


def get_values_from_record(record_):
    return [x.item() if isinstance(x, np.generic) else x for x in record_.values]


def generate_insert_query_template(record_):
    return f"INSERT INTO cars(price, brand, fuel, power, prod_year) VALUES ({','.join(['%s'] * len(record_))})"


def run_query(query_template, values_):
    cursor.execute(query_template, values_)
    conn.commit()


# for i in range(len(df)):
#     record = get_row_from_df(df, i)
#     values = get_values_from_record(record)
#     query = generate_insert_query_template(record)
#     run_query(query, values)

"""ZADANIE 3
Napisz funkcję, która przyjmie zapytanie typu SELECT i wykona je na bazie.
"""

"""ZADANIE 4
Napisz funkcję, która przyjmie id wiersza w tabeli, nazwę kolumny oraz nową wartość a następnie zupdatuje tabelę.
"""

"""ZADANIE 5
Napisz funkcję, która przyjmie id wiersza w tabeli a następnie go usunie.
"""
