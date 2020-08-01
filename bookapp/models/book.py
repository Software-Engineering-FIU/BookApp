from datetime import datetime
from flask import current_app

from .. import db, login_manager

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

#filter by book genre
#@app.route('/filter_by_genre/<genre>', methods=['GET'])
#def bookGenre(genre):
#    book = Book.query.get_or_404(genre)

#filter by top sellers
#@app.route('/filter_by_sold/<int:sold>', methods=['GET'])
#def getTopSold(sold):
#    Book.query.order_by(Book.copies_sold).limit(sold)

#filter by rating, need book average ratings
#@app.route('/filter_by_rating/<int:rating>', methods=['GET'])
#def bookRating(rating):
#    Book.query()

#@app.route('/show_list/<int:x>', methods=['GET'])
#def getList(x):
#   Book.query.limit(x).all()

#     def __init__ (self, id, isbn, name, description, price, genre, publisher, year_published, copies_sold, author_id):
#         self.id = id
#         self.isbn= isbn
#         self.name = name
#         self.description = description
#         self.price = price
#         self. genre = genre
#         self. publisher = publisher
#         self.year_published = year_published
#         self.copies_sold = copies_sold
#         self.author_id = author_id
#
#class BookSchema(ma.Schema):
#     class Meta:
#         fields = ('isbn', 'name', 'description', 'price', 'genre', 'publisher', 'year_published', 'copies_sold')

    def __repr__(self):
        return f"Book('{self.name}', '{self.isbn}', '{self.price}', '{self.author}','{self.genre}')"

book_schema = BookSchema(strict=True)
books_schema = BookSchema(many=True, strict=True)




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

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer(), nullable=False)
    date = db.Column(db.String(80), nullable=False, default=datetime.utcnow)
    comment = db.Column(db.String(120), unique=True)
    #Relationships
    book_id = db.Column(db.ForeignKey('book.id'))  #! 1-M (D)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)  #! 1-M (A)

    def __repr__(self):
        return f"Review('{self.username}', '{self.email}')"