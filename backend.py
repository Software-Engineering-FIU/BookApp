from datetime import datetime
from route import app
from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:toor@localhost/book-app'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password =  db.Column(db.String(8), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True)          # * Email, name, and address are optional 
    name = db.Column(db.String(120), unique=True)
    home_address = db.Column(db.String(120), unique=True)
    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"



class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer(), nullable=False)
    date = db.Column(db.String(80), nullable=False, default=datetime.utcnow)
    comment = db.Column(db.String(120), unique=True)
    book = db.Column(db.ForeignKey('Book'))
    user = db.Column(db.ForeignKey('User'))
    def __repr__(self):
        return f"Review('{self.username}', '{self.email}')"

class CreditCard(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    credit_num = db.Column(db.Sting(20), unique=True)
    user = db.Column(db.ForeignKey('User'))
    def __repr__(self):
        return f"CreditCard('{self.user}', '{self.credit_num}')"

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    isbn = db.Column(db.String(80), unique=True)
    name = db.Column(db.String(120), unique=True)
    description = db.Column(db.String(120), unique=True)
    price = db.Column(db.Integer)
    author = db.ForeignKey('Author')
    genre = db.Column(db.String(15))
    publisher = db.Column(db.String(20))
    year_published = db.Column(db.Date)
    copies_sold = db.Column(db.Integer)
    def __repr__(self):
        return f"Book('{self.name}', '{self.isbn}', '{self.price}', '{self.author}','{self.genre}')"
class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(15))
    last_name = db.Column(db.String(15))
    biography = db.Column(db.String(120), unique=True)
    publisher = db.Column(db.String(20))
    def __repr__(self):
        return f"Author('{self.last_name}', '{self.first_name}')"

def create_tables():
    db.create_all()