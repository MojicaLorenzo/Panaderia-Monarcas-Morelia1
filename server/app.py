#!/usr/bin/env python3

# Standard library imports
from flask import make_response, request
from models import Item, Cart, Customer, Bakery, Review
from config import app

# Remote library imports
from flask import request
from flask_restful import Resource

# Local imports
# Add your model imports


# Views go here!

@app.route('/')
def index():
    return '<h1>Project Server</h1>'

@app.route('/items', methods = ['GET'])
def items():
    # if request.method == 'GET':
    #     items = Item.query.all()
    #     resp = [item.to_dict() for item in items]
    #     return make_response (resp, 200)
    return '<h1>items go here</h1>'


if __name__ == '__main__':
    app.run(port=5555, debug=True)

