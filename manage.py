import os

from flask import jsonify
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from bookapp import create_app, db
from bookapp.models import users, Book

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)
migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)

@app.route('/book', methods=['GET'])
def get_book():
    all_book = Book.query.all()
    result = book.dump(all_book)
    return jsonify(result.data)

if __name__ == '__main__':
    manager.run()

