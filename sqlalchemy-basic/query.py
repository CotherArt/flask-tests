import db
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=db.engine)
session = Session()

# All data
for s in session.query(db.transactions).all():
    print(s.transaction_id, s.price)
    
print('*' * 20)
print('Transactions with price over 40:')

# selected data
for s in session.quety(db.transactions).filter(db.transactions.price>40):
    print(s.transaction_id, s.price)