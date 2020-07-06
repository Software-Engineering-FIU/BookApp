from route import app
from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:toor@localhost/book-app'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)
    password =  db.Column(db.String(8), unique=True)
    name = db.Column(db.String(120), unique=True)
    home_address = db.Column(db.String(120), unique=True)
    

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(80), unique=True)
    comment = db.Column(db.String(120), unique=True)
    

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    isbn = db.Column(db.String(80), unique=True)
    name = db.Column(db.String(120), unique=True)
    description = db.Column(db.String(120), unique=True)
    price = db.Column(db.Integer)
    author = db.Column(db.String(40))
    genre = db.Column(db.String(15))
    publisher = db.Column(db.String(20))
    year_published = db.Column(db.Date)
    copies_sold = db.Column(db.Integer)

class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(15))
    last_name = db.Column(db.String(15))
    biography = db.Column(db.String(120), unique=True)
    publisher = db.Column(db.String(20))

def create_tables():
    db.create_all()