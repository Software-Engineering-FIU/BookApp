from flask import current_app
from cart.py import addToCart #rename when cart api is made
from bookapp.dao import DatabaseAccess

# WishList -> TableName
# ID (unique) -> int (primary key)
# UserID -> int (foriegn key)
# BookID -> int multi-value attribute/relational data
# ShoppingID -> int
# Name (unique) -> string

class Wishlist (DatabaseAccess):

    def __init__(self):
        super(Wishlist, self).__init__()

    def createList (user_id, name):
        try:
            testQuery = ("select Name from WishList where WishList.UserID = User.ID and User.ID = '{}'").format(user_id)
            testList = super(Wishlist, self).read(query=testQuery)
            if name not in testList:
                helperQuery = "select ID from ShoppingCart where ShoppingCart.UserID = User.ID and User.ID = '{}'").format(user_id)
                cart_id = super(Wishlist, self).read(query=helperQuery)
                query = "insert into WishList (UserID, ShoppingID, Name) values ('{}','{}','{}')".format(user_id, cart_id, name)  #create a new list, ID will auto increment, and bookID is blank until some book is added
                super(Wishlist, self).read(query=query)
        except Exception as e:
            print(e, 'list with this name already exists')
            return []

    def displayList (self, list_id):
        try:
            query = ("select w.*,b.ID, title, author, publisher, price "
                     "from WishList as w left join books as b "
                     "on b.ID=w.BookID where w.ID='{}'").format(list_id)
            result = super(Wishlist, self).read(query=query)
            return result
        except Exception as e:
            print(e, 'list_id does not exist')
            return []

    def addToList (self, book_id, list_id)
        try:
            testQuery = ("select exists( w.BookID, b.ID "
                         "from WishList as w inner join Book as b on b.ID=w.BookID"
                         "where w.ID='{}')").format(list_id)
            testAdd = super(Wishlist, self).read(query=testQuery)
            if testAdd = 'true':
                query = ("insert into WishList (book_id) values ('{}') where WishList.ID = '{}'").format(book_id, list_id)
                super(Wishlist, self).read(query=query)
                # do I need a return statement?
        except Exception as e:
            print(e, 'already in wishlist')
            return []

    def removeFromList(self, book_id, list_id):
        query = ("delete from WishList where BookID = '{}' and ID = '{}'").format(book_id, list_id)
        super(Wishlist, self).read(query=query)

    def sendToCart(self, book_id, list_id, cart_id):
        removeFromList(self, book_id, list_id)
        addToCart(self, book_id, cart_id)
        # @cart_id is placeholder until addToCart function is made by Drew?

