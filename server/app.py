#!/usr/bin/env python3

# Standard library imports
from flask import make_response, request
from models import Item, Cart, Customer, Bakery, Review
from config import db, app, bcrypt

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
    if request.method == 'GET':
        items = Item.query.all()
        resp = [item.to_dict() for item in items]
        return make_response (resp, 200)
    
#----------------------------------------
# ITEMS BY ID
#----------------------------------------
@app.route('/items/<int:id>', methods=['GET', 'POST', 'PATCH', 'DELETE'])
def item_by_id(id):
    item_by_id = Item.query.filter_by(id = id).first()
    if item_by_id:

# ---------------- GET -----------------------
        if request.method == 'GET':
            resp = make_response(item_by_id.to_dict(), 200)

#----------------- POST-----------------------
        elif request.method == 'POST':
            form_data = request.get_json()
            try:
                new_item_obj = Item(
                    name = form_data['name'],
                    type = form_data['type'],
                    description = form_data['description'],
                    price = form_data['price'],
                    quantity = form_data['quantity'],
                    image = form_data['image']
                    ###  add some functionality to automatically mark which store id  ###
                )
                db.session.add(new_item_obj)
                db.session.commit()
                resp = make_response(new_item_obj.to_dict(), 201)
            except ValueError:
                resp = make_response({ "errors" : ["Validation Errors!"]}, 400)

#---------------- PATCH-----------------------
        elif request.method == 'PATCH':
            form_data = request.get_json()
            try:
                for attr in form_data:
                    setattr(item_by_id, attr, form_data.get(attr))
                db.session.commit()
                resp = make_response(item_by_id.to_dict(), 202)
            except ValueError:
                resp = make_response({ "errors": ["Validation Errors"]}, 400)

# --------------- DELETE -------------------------
        elif request.method == 'DELETE':
            db.session.delete(item_by_id)
            db.session.commit()
            resp = make_response({}, 204)

    else:
        resp = make_response({"error": "No Item found!"})
    return resp

#----------------------------------------
# ALL CUSTOMERS
#----------------------------------------

@app.route('/customers', methods=['GET', 'POST'])
def customers():
    customers = Customer.query.all()
# ---------------- GET -----------------------
    if request.method == 'GET':
        return make_response([customer.to_dict(rules=('-carts', )) for customer in customers], 200)
    
# ---------------- POST -----------------------
    elif request.method == 'POST':
        form_data = request.get_json()
        try:
            new_customer_obj = Customer(
                name = form_data['name'],
                username = form_data['username'],
                email = form_data['email'],
                password = form_data['password'],
            )
            db.session.add(new_customer_obj)
            db.session.commit()
            resp = make_response(new_customer_obj.to_dict(), 201)
            return resp
        except ValueError:
            resp = make_response({ "errors": ["Validation Errors!"]}, 400)
    return resp

#----------------------------------------
# CUSTOMERS BY ID
#----------------------------------------

@app.route('/customers/<int:id>', methods=['GET', 'PATCH', 'DELETE'])
def customer_by_id(id):
    customer = Customer.query.filter_by(id = id).first()
    if customer:

# ---------------- GET -----------------------
        if request.method == 'GET':
            resp = make_response(customer.to_dict(), 200)

#---------------- PATCH-----------------------
        elif request.method == 'PATCH':
            form_data = request.get_json()
            try:
                for attr in form_data:
                    setattr(customer, attr, form_data.get(attr))
                db.session.commit()
                resp = make_response(customer.to_dict(), 202)
            except ValueError:
                resp = make_response({ "errors": ["Validation Errors"]}, 400)

# --------------- DELETE -----------------------
        elif request.method == 'DELETE':
            db.session.delete(customer)
            db.session.commit()
            resp = make_response({}, 204)

    else:
        resp = make_response({"error" : "No Customer Found!"}, 404)    
    return resp


if __name__ == '__main__':
    app.run(port=5555, debug=True)

