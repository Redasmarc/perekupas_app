from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

engine = create_engine("sqlite:///perekupas.db")
Base = declarative_base()

class Masinos(Base):
    __tablename__ = "masinos"

    id = Column(Integer, primary_key=True)
    make = Column("Marke", String)
    model = Column("Modelis", String)
    buy_price = Column("Pirkimo kaina", Float)
    fix_price = Column("Remonto kaina", Float)
    sell_price = Column("Pardavimo kaina", Float)
    buy_date = Column("Nupirkimo data", DateTime)
    sell_date = Column("Pardavimo data", DateTime)
    profit = Column("Pelnas", Float)
    pardavejas = relationship("Pardavejas", back_populates="masinos")
    
    def __init__(self, make, model, buy_price, fix_price, sell_price, buy_date, sell_date, profit):
        self.make = make
        self.model = model
        self.buy_price = buy_price
        self.fix_price = fix_price
        self.sell_price = sell_price
        self.buy_date = buy_date
        self.sell_date = sell_date
        self.profit = profit

    def __str__(self):
        return f"{self.make}, {self.model}, {self.buy_price}, {self.fix_price}, {self.sell_price}, {self.buy_date}, {self.sell_date}, {self.profit}"

class Pardavejas(Base):
    __tablename__ = "pardavejas"

    id = Column(Integer, primary_key=True)
    f_name = Column("Pardavejo vardas", String)
    l_name = Column("Pardavejo pavarde", String)
    profit_made = Column("Viso uzdirbta", Float, ForeignKey="masinos.profit")
    salary = Column("Atlyginimas", Float)
    masinos = relationship("Masinos", back_populates="pardavejas")

    def __init__(self, f_name, l_name, profit_made, salary):
        self.f_name = f_name
        self.l_name = l_name
        self.profit_made = profit_made
        self.salary = salary

    def __str__(self):
        return f"{self.f_name}, {self.l_name}, {self.profit_made}, {self.salary}"


Base.metadata.create_all(engine)