from flask import app
from bookapp.models import Book

# /user/login
# /user/logout
# /books

#* filter by book genre

@app.route('/filter_by_genre/<genre>', methods=['GET'])
def filterGenre(genre):
   return Book.filter_by(genre=genre)

#* filter by top sellers
@app.route('/filter_by_sold/<int:sold>', methods=['GET'])
def filterTopSold(sold):
    return Book.query.order_by(Book.copies_sold).limit(sold)

#* filter by rating, need book average ratings
#@app.route('/filter_by_rating/<int:rating>', methods=['GET'])
#def bookRating(rating):
#    return Book.query()

@app.route('/show_list/<int:x>', methods=['GET'])
def getList(x):
   return Book.query.limit(x).all()

# /books/detail/{id}
# /wishlist

# /user/*
# /books/*
