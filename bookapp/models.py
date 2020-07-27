# models of your application
# WishList, User, Book, 


# need other models to make work
class WishList (db.Model):
    id = db.Column(db.Integer, primary_key = True, nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.ID'))
    name = db.Column(db.St0ring(255), unique = True, nullable = False)
    shopping_id = db.Column(db.Integer, db.ForeignKey('ShoppingCart.ID'))
    book_list = db.relationship("WishList", secondary = "onWishList", backref = 'list_id')

#association table for books on a wishlist
onWishList = db.Table ('onWishList'
    db.Column('list_id', db.Integer, db.ForeignKey('WishList.ID')),
    db.Column('book_id', db.Integer, db.ForeignKey('Book.ID'))
    )
