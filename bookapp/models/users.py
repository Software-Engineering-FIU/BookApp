from flask import current_app

from .. import db, login_manager

#User -> TableName
#ID (unique) -> Int
#FirstName -> String
#LastName -> String
#Email -> String 
#Password -> String
#Optional Fields

class Users(db.Model):
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
    wishlists = db.relationship('Wishlist', backref='list_owner') #! 1-M (F)

    def __repr__(self): #* __repr__ is similar to a toString method
        return f"User('{self.username}', '{self.email}')"


@login_manager.user_loader
def user_loader(user_id):
    return Users.query.get(user_id)

    
