from flask import session
import db
from sqlalchemy.orm import sessionmaker

# new session
Session = sessionmaker(bind=db.engine)
session = Session()

def insert_user(user, password):
    tr = db.usuarios(user, password)
    session.add(tr)
    # save changes in data base
    session.commit()

    print('+ user: {} password: {}'.format(user, password))
    
def insert_producto(nombre, cantidad):
    tr = db.usuarios(nombre, cantidad)
    session.add(tr)
    session.commit()