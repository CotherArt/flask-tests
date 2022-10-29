from sqlalchemy import Column, create_engine, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from pathlib import Path

engine = create_engine('sqlite:///database.sqlite', echo=True)
base = declarative_base()

class usuarios (base):
    __tablename__ = 'usuarios'
    
    user_id = Column(Integer, primary_key=True) # Autoincremental por defecto
    username = Column(String)
    password = Column(String)
    
    def __init__ (self, username, password):
        self.username = username
        self.password = password

class productos(base):
    __tablename__ = 'productos'
    
    producto_id = Column(Integer, primary_key=True)
    nombre = Column(String)
    precio = Column(Integer)
    
    def __init__ (self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

def create_db():
    # Creates the database
    base.metadata.create_all(engine)
    print('database.sqlite creado!')
    
if not Path('database.sqlite').exists():
    print('database.sqlite no exite')
    print('creando database.sqlite...')
    create_db()