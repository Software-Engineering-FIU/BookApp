from datetime import datetime
from route import app
from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:toor@localhost/book-app'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password =  db.Column(db.String(8), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True)  #* Email, name, and address are optional 
    name = db.Column(db.String(120), unique=True)
    home_address = db.Column(db.String(120), unique=True)
    #Relationships
    cart = db.relationship('Cart', backref='cart_user', uselist=False)   #! 1-1 (B)
    #* One-to-one relationship with cart
    reviews = db.relationship('Review', backref='post_author') #! 1-M (A)
    #* backref creates column 'post_author for Posts
    cards = db.relationship('Card', backref='card_owner')   #! 1-M (C)
    wishlists = db.relatioship('Wishlist', backref='list_owner') #! 1-M (F)

    def __repr__(self): #* __repr__ is similar to a toString method
        return f"User('{self.username}', '{self.email}')"

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer(), nullable=False)
    date = db.Column(db.String(80), nullable=False, default=datetime.utcnow)
    comment = db.Column(db.String(120), unique=True)
    #Relationships
    book_id = db.Column(db.ForeignKey('book.id'))  #! 1-M (D)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)  #! 1-M (A)

    def __repr__(self):
        return f"Review('{self.username}', '{self.email}')"

class Card(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    credit_num = db.Column(db.Sting(20), unique=True, nullable=False)
    #Relationships
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)  #! 1-M (C)

    def __repr__(self):
        return f"CreditCard('{self.user}', '{self.credit_num}')"

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    isbn = db.Column(db.String(80), unique=True)
    name = db.Column(db.String(120), unique=True)
    description = db.Column(db.String(120), unique=True)
    price = db.Column(db.Integer)
    genre = db.Column(db.String(15))
    publisher = db.Column(db.String(20))
    year_published = db.Column(db.Date)
    copies_sold = db.Column(db.Integer)
    #Relationships
    author_id = db.Column(db.Integer,db.ForeignKey('author.id')) #! 1-M (E)
    #? Could be a M-M relationship, but
    #wishlists = db.relationship('Wishlist', )  #! M-M (G)
    #?book and wishlist is a M-M relationship; not sure how to code M-M
    reviews = db.relationship('Review', backref='book_reviewed')    #! 1-M (D)

    def __repr__(self):
        return f"Book('{self.name}', '{self.isbn}', '{self.price}', '{self.author}','{self.genre}')"

class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(15))
    last_name = db.Column(db.String(15))
    biography = db.Column(db.String(120), unique=True)
    publisher = db.Column(db.String(20))
    #Relationships
    books_written = db.relationship('Book', backref='author')   #! 1-M (E)
    #? Could be a M-M relationship

    def __repr__(self):
        return f"Author('{self.last_name}', '{self.first_name}')"

class Cart(db.model):
    id = db.Column(db.Integer, primary_key=True)
    #Relationships
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) #! 1-1 (B)

class Wishlist(db.model):
    id = db.Column(db.Integer, primary_key=True)
    #Relationships
    #book_id = db.Column(db.Integer, db.ForeignKey('book.id')) #! M-M (G)
    #?book and wishlist is a M-M relationship; not sure how to code M-M
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id')) #! 1-M (F)

def create_tables():
    db.create_all()