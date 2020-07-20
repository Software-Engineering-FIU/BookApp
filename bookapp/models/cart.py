from flask import current_app

from .. import db, login_manager

class Card(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    credit_num = db.Column(db.String(20), unique=True, nullable=False)
    #Relationships
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)  #! 1-M (C)

    def __repr__(self):
        return f"CreditCard('{self.user}', '{self.credit_num}')"


class Cart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    #Relationships
    user_id = db.Column(db.Integer, db.ForeignKey('users.id')) #! 1-1 (B)

class Wishlist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    #Relationships
    #book_id = db.Column(db.Integer, db.ForeignKey('book.id')) #! M-M (G)
    #?book and wishlist is a M-M relationship; not sure how to code M-M
    owner_id = db.Column(db.Integer, db.ForeignKey('users.id')) #! 1-M (F)

def create_tables():
    db.create_all()