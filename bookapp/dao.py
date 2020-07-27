from contextlib import closing
from flask import jsonify
from bookapp.connectDB import connectDB

class DatabaseAccess(object):

    _instance = None

    def __init__(self):
        #constructor
        self.connection = connectDB().get_connection()

    def read(self, table=None, columns=None, where_row=None, query=None):
        with closing(self.connection.cursor()) as cursor:
            cursor.execute(query)
            data_list = cursor.fetchall()
            return data_list
