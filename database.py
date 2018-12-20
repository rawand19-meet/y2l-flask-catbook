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
	 if request.method == 'GET':
        return render_template('form.html')
    else:
        name = request.form['firstname']
        animal = request.form['animal']


        save_to_database(name, animal)        
        return render_template('response.html',
            n = name,
            a = animal)


	cat = session.query(Cat).filter_by(id=id).first()
	return cat

def add_vote(id)
 if request.method == 'GET':
        return ''
    else:
        return 'You just made a POST request!'



create_cat("JO","https://data.whicdn.com/images/51239572/original.jpg",1000)
