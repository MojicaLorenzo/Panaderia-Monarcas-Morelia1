#!/usr/bin/env python3

# Standard library imports
from flask import make_response, request, session
from flask import jsonify
from models import Item, Cart, Customer, Bakery, Review, Cart_item
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

@app.route('/check_session', methods=['GET'])
def check_session():
    # Check current session
    customer_id = session.get('customer_id')

    if customer_id:
        customer = Customer.query.filter(Customer.id == customer_id).first()

        if customer:
            # If the user has a cart, retrieve it; otherwise, create a new cart
            cart = Cart.query.filter_by(customer_id=customer.id).first()
            if not cart:
                cart = Cart(customer=customer)
                db.session.add(cart)
                db.session.commit()

            # Store the cart's ID in the session
            session['cart_id'] = cart.id

            resp = make_response(customer.to_dict(), 200)
            return resp

    resp = make_response({}, 404)
    return resp

# @app.route('/check_session', methods = ['GET'])
# def check_session():
#     # check current session
#     customer_id = session['customer_id']

#     customer = Customer.query.filter(Customer.id == customer_id).first()

#     if customer:
#         resp = make_response( customer.to_dict(), 200)
#         return resp
#     else:
#         resp = make_response({}, 404)
#         return resp

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
            session['customer_id'] = customer.id

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
        resp = [item.to_dict(rules=('-bakery', '-reviews', '-cart_items', '-bakery_id')) for item in items]
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
            resp = make_response(item_by_id.to_dict(rules=('-bakery', '-reviews', '-cart')), 200)

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
            print(form_data)
            # password = form_data['password']
            try:
                for attr in form_data:
                    setattr(customer, attr, form_data.get(attr))

                customer.password_hash = form_data["password"]
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
    print(carts)
# ---------------- GET -----------------------
    if request.method == 'GET':
        return make_response([cart.to_dict(rules = ('-cart_items.cart.customer.reviews', '-cart_items.cart.customer.password_hash', '-customer')) for cart in carts], 200)
    

@app.route('/cart_items', methods = ['GET'])
def cart_items():
    cart_items = Cart_item.query.all()
    print(cart_items)

    resp = [cart_item.to_dict(rules=('-cart.customer.reviews', '-cart.customer._password_hash', '-cart.reviews')) for cart_item in cart_items]

    return make_response(resp, 200)

#----------------------------------------
# CART CRUD
#----------------------------------------

# ---------------- GET ---------------------------------------------
# @app.route('/cart', methods=['GET'])
# def get_cart():
#     customer_id = session.get('customer_id')
#     print(customer_id)

#     if not customer_id:
#         return make_response({'error': 'Customer not logged in'}, 401)

#     cart = Cart.query.filter_by(customer_id=customer_id).first()
#     resp = [item.to_dict() for item in cart.items]

#     return make_response(resp, 200)

# @app.route('/cart', methods=['GET'])
# def get_cart():
#     customer_id = session.get('customer_id')

#     if not customer_id:
#         return make_response({'error': 'Customer not logged in'}, 401)

#     cart = Cart.query.filter_by(customer_id=customer_id).first()

#     if not cart:
#         return make_response({'error': 'Cart not found'}), 404

#     cart_items = [item.to_dict() for item in cart.items]
#     return make_response({'items': cart_items}), 200

@app.route('/cart', methods=['GET'])
def get_cart():
    customer_id = session.get('customer_id')

    if not customer_id:
        return make_response({'error': 'Customer not logged in'}, 401)

    cart = Cart.query.filter_by(customer_id=customer_id).first()

    if not cart:
        return make_response({'error': 'Cart not found'}, 404)

    resp = [item.to_dict() for item in cart.items]
    return make_response(resp, 200)

# --------------------POST------------------------------------------
@app.route('/cart/add', methods=['POST'])
def add_to_cart():
    customer_id = session.get('customer_id')

    if not customer_id:
        return make_response({'error': 'Customer not logged in'}, 401)

    form_data = request.get_json()
    item_id = form_data.get('item_id')

    # Validate

    cart = Cart.query.filter_by(customer_id=customer_id).first()

    if not cart:
        return make_response({'error': 'Cart not found'}, 404)

    item = Item.query.get(item_id)

    if not item:
        return make_response({'error': 'Item not found'}, 403)

    # Add the item to the cart
    cart_item = Cart_item(item=item, cart=cart)
    db.session.add(cart_item)
    db.session.commit()

    return make_response({'message': 'Item added to cart successfully'}, 201)

# --------------------DELETE-----------------------------------------------
@app.route('/cart/remove/<int:item_id>', methods=['DELETE'])
def remove_from_cart(item_id):
    customer_id = session.get('customer_id')

    if not customer_id:
        return make_response({'error': 'Customer not logged in'}, 401)

    cart = Cart.query.filter_by(customer_id=customer_id).first()

    if not cart:
        return make_response({'error': 'Cart not found'}, 404)

    cart_item = Cart_item.query.filter_by(cart_id=cart.id, item_id=item_id).first()

    if not cart_item:
        return make_response({'error': 'Item not found in the cart'}, 404)

    db.session.delete(cart_item)
    db.session.commit()

    return make_response({'message': 'Item removed from the cart successfully'}), 204



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

