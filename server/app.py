#!/usr/bin/env python3

# Standard library imports
from flask import make_response, request, session
from models import Item, Cart, Customer, Bakery, Review
from config import app, db

# Remote library imports
from flask import request
from flask_restful import Resource

# Local imports
# Add your model imports


# Views go here!

@app.route('/')
def index():
    return '<h1>Project Server</h1>'

# ----------------------------------------
# customer/user SESSION, LOGIN, AND LOGOUT
# ----------------------------------------

@app.route('/check_session', methods = ['GET'])
def check_session():
    # check current session
    customer_id = session['customer_id']

    customer = Customer.query.filter(Customer.id == customer_id).first()

    if customer:
        resp = make_response( customer.to_dict(), 200)
        return resp
    
    else:
        resp = make_response({}, 404)
        return resp

@app.route('/login', methods = ['POST'])
def login():
    
    form_data = request.get_json()

    username = form_data['username']
    password = form_data['password']

    customer = Customer.query.filter(Customer.username == username).first()

    if customer:
        # authenticate customer
        is_authenticate = customer.authenticate(password)

        if is_authenticate:
            session['customer.id'] = customer.id

            resp = make_response(customer.to_dict(), 201)
            return resp
        else:
            resp = make_response({"error" : "customer cannot log in"})
        
    else:
        resp = make_response({"error": "customer not found"}, 404)
        # print(session)
        return resp

@app.route('/logout', methods = ['DELETE'])
def logout():
    # remove session
    session['customer_id'] = None

    resp = make_response({}, 204)
    # print(session)
    return resp

# ----------------------------------------
# customer/user SESSION, LOGIN, AND LOGOUT ^^^^
# ----------------------------------------

@app.route('/items', methods = ['GET'])
def items():
    if request.method == 'GET':
        items = Item.query.all()
        resp = [item.to_dict(rules=('-bakery', '-reviews', '-carts', '-bakery_id')) for item in items]
        return make_response (resp, 200)
    
# ----------------------------------------
# ITEMS BY ID
# ----------------------------------------
@app.route('/items/<int:id>', methods=['GET', 'POST', 'PATCH', 'DELETE'])
def item_by_id(id):
    item_by_id = Item.query.filter_by(id = id).first()
    if item_by_id:

# ---------------- GET -----------------------
        if request.method == 'GET':
            resp = make_response(item_by_id.to_dict(rules=('-bakery', '-reviews', '-carts')), 200)

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
        return make_response([customer.to_dict(rules=('-carts', 
            '-reviews', '-password_hash')) for customer in customers], 200)
    
# ---------------- POST -----------------------
    elif request.method == 'POST':
        form_data = request.get_json()

        username = form_data['username']
        password = form_data['password']
        try:
            new_customer = Customer(
                name = form_data['name'],
                username = username,
                email = form_data['email'],     
                # _password_hash = form_data['password'],
                # comment out this password
            )
            # uncomment this password
            new_customer.password_hash = password
            

            db.session.add(new_customer)
            db.session.commit()
            # sets signed in customer to session
            # session['customer_id']= new_customer.id

            resp = make_response(new_customer.to_dict(), 201)
            return resp
        except ValueError:
            resp = make_response({ "errors": ["Create User!"]}, 400)
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

#----------------------------------------
# ALL REVIEWS
#----------------------------------------

@app.route('/reviews', methods=['GET', 'POST'])
def reviews():
    reviews = Review.query.all()
# ---------------- GET -----------------------
    if request.method == 'GET':
        return make_response([review.to_dict(rules=('-customer', '-item')) for review in reviews], 200)



#----------------------------------------
# ALL CARTS
#----------------------------------------

@app.route('/carts', methods=['GET', 'POST'])
def carts():
    carts = Cart.query.all()
# ---------------- GET -----------------------
    if request.method == 'GET':
        return make_response([cart.to_dict(rules = ('-customer.reviews', '-customer.password_hash')) for cart in carts], 200)
    

#----------------------------------------
# BAKERY BY ID
#----------------------------------------
@app.route('/bakery/<int:id>', methods=['GET'])
def bakery_by_id(id):
    bakery = Bakery.query.filter_by(id = id).first()
    if bakery:

# ---------------- GET -----------------------
        if request.method == 'GET':
            resp = make_response(bakery.to_dict(rules = ('-items',)), 200)
    return resp



if __name__ == '__main__':
    app.run(port=5555, debug=True)

