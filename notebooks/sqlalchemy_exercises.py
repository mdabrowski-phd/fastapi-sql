"""ZADANIA"""

import pandas as pd
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

"""ZADANIE 1
Utwórz klasę odpowiadającą tabeli cars a następnie samą tabelę za pomocą SQLAlchemy.
"""

df = pd.read_csv("cars.csv", usecols=["price", "brand", "fuel", "power", "prod_year"]).dropna()
print(df.head())

user = "postgres"
password = "postgres"
host = "localhost"
port = "5432"
database = "postgres"


Base = declarative_base()

connection_string = f"postgresql://{user}:{password}@{host}:{port}/{database}"
engine = create_engine(connection_string)

Session = sessionmaker(bind=engine)
session = Session()


class CarTable(Base):
    __tablename__ = "cars"

    id_number = Column("id", Integer, primary_key=True)
    price = Column("price", Integer, nullable=False)
    brand = Column("brand", String, nullable=False)
    fuel = Column("fuel", String)
    power = Column("power", Integer)
    prod_year = Column("prod_year", Integer, nullable=False)

    def __repr__(self):
        return f"Car(id={self.id_number})"


# Base.metadata.create_all(bind=engine)

"""ZADANIE 2
Napisz kod, który doda do tabeli wiersz z dataframe'a wykorzystując SQLAlchemy.
"""

# for i in range(len(df)):
#     print(df.loc[i].to_dict())
#     task = CarTable(**df.loc[i].to_dict())
#     session.add(task)
#
# session.commit()

"""ZADANIE 3
Napisz kod, który wyciągnie dane z dataframe'a na różne sposoby
"""

# *** SELECT **
results = session.query(CarTable).all()
print(results)
print(results[0].price)

results = session.query(CarTable).first()
print(results)

results = session.query(CarTable.price, CarTable.brand).all()
print(results)

# *** FILTER (WHERE) ***
results = session.query(CarTable).filter(CarTable.price < 10_000).all()
print(results)

results = session.query(CarTable).filter_by(prod_year=2012).all()
print(results)
