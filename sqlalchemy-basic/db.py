from sqlalchemy import Column, create_engine, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///sqlalchemy.sqlite', echo=True)
base = declarative_base()

class transactions (base):
    __tablename__ = 'transactions'
    
    transaction_id = Column(Integer, primary_key=True)
    date = Column(String)
    item_id = Column(Integer)
    price = Column(Integer)
    
    def __init__ (self, transaction_id, date, item_id, price):
        self.transaction_id = transaction_id
        self.date = date
        self.item_id = item_id
        self.price = price
        
# Creates the database
base.metadata.create_all(engine)