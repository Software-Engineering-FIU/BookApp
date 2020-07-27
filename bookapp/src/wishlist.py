from flask import current_app
from cart.py import addToCart #rename when cart api is made
from bookapp.dao import DatabaseAccess

# WishList -> TableName
# ID (unique) -> int (primary key)
# UserID -> int (foriegn key)
# BookID -> int
# ShoppingID -> int
# Name (unique) -> string

class Wishlist (DatabaseAccess):

    def __init__(self):
        super(Wishlist, self).__init__()

    def DisplayList (self, list_id):
        try:
            query = ("select w.*,b.ID, title, author, publisher, price "
                     "from wishlist as w left join books as b "
                     "on b.ID=w.BookID where list_id='{}'").format(list_id)
            result = super(Wishlist, self).read(query=query)
            return result
        except Exception as e:
            print(e, 'list_id does not exist')
            return []

    def addToList (self, book_id, list_id)
        try:
            testQuery = ("select exists( w.BookID, b.ID "
                         "from wishlist as w inner join books as b on b.ID=w.BookID"
                         "where list_id='{}')").format(list_id)
            testAdd = super(Wishlist, self).read(query=testQuery)
            if testAdd = 'true':
                query = ("insert into wishlist (book_id) values ('{}') where list_id = '{}'").format(book_id, list_id)
                super(Wishlist, self).read(query=query)
                # do I need a return statement?
        except Exception as e:
            print(e, 'already in wishlist')
            return []

    def removeFromList(self, book_id, list_id):
        query = ("delete from wishlist where book_id = '{}' and list_id = '{}'")

    def sendToCart(self, book_id, list_id, param):
        removeFromList(self, book_id, list_id)
        addToCart(self, param)
        # @param is whatever parameter I need for the addToCart function

