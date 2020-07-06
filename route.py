from enum import unique
from flask import Flask, request, jsonify
from flask import json
import backend

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return '<h1>Welcome</h1>'

if __name__ == "__main__":
    backend.create_tables()
    app.run(debug=True)
