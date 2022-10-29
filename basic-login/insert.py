from flask import session
import db
from sqlalchemy.orm import sessionmaker

# new session
Session = sessionmaker(bind=db.engine)
session = Session()

def insert_user(username, password):
    tr = db.usuarios(username, password)
    session.add(tr)
    # save changes in data base
    session.commit()

    print('+ username: {} password: {}'.format(username, password))
    
def insert_producto(nombre, cantidad):
    tr = db.usuarios(nombre, cantidad)
    session.add(tr)
    session.commit()