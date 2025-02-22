from models import Dog
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

   
engine = create_engine('sqlite:///:memory:')

def create_table(Base, engine):
     Base.metadata.create_all(engine)
    
def save(session, dog):
    session.add(dog)
    session.commit()

def get_all(session):
    return session.query(Dog).all()

def find_by_name(session, name):
    return session.query(Dog.name).first()

def find_by_id(session, id):
    return session.query(Dog).filter(Dog.id == id).first()

def find_by_name_and_breed(session, name, breed):
    return session.query(Dog).filter(Dog.name == name, Dog.breed ==breed).first()

def update_breed(session, dog, breed):
    return session.query(Dog).filter(Dog.id == dog.id).update({Dog.breed: breed})






