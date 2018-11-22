from models import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///cats.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def create_cat(name , image, votes):
    cat_object = Cat(name=name, image=image, votes=votes)
    session.add(cat_object)
    session.commit()


def get_all_cats():
    cats = session.query(Cat).all()
    return cats

def get_cat(id):

	cat = session.query(Cat).filter_by(id=id).first()
	return cat

