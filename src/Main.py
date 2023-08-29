from sqlalchemy import create_engine
import datetime as dt
from sqlalchemy import Column, Date, Integer, Text, create_engine, inspect
from sqlalchemy.orm import sessionmaker, registry
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
engine = create_engine('sqlite:///data/vivino.db')
mapper_registry = registry()
Base = mapper_registry.generate_base()
Maker = sessionmaker()
session = Maker(bind= engine)
metadata = engine.MetaData()
# declarative base class
Base = declarative_base()
%load_ext sql
# an example mapping using the base
class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    nickname = Column(String)

%%sql
SELECT
    vintages.ratings_average,
    vintages.ratings_count,
    vintages.name,
    vintages.price_euros
FROM
    vintages
WHERE
    vintages.price_euros BETWEEN 20 AND 30
ORDER BY
    vintages.ratings_average DESC,
    vintages.ratings_count DESC
;