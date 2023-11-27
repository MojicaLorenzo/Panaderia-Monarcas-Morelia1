from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.orm import validates
import re
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.ext.hybrid import hybrid_property
from config import bcrypt, db

# Models go here!

class Item (db.Model, SerializerMixin):
    __tablename__ = "items"

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)
    type = db.Column(db.String)
    description = db.Column(db.String)
    price = db.Column(db.Float)
    quantity = db.Column(db.Integer)
    image = db.Column(db.String)

    #----------------------foreign-keys----------------------------------
    bakery_id = db.Column(db.Integer, db.ForeignKey('bakery.id'))

    #----------------------relationships---------------------------------
    bakery = db.relationship('Bakery', back_populates = 'items')
    reviews = db.relationship('Review', back_populates = 'item', cascade = 'all, delete-orphan')
    # carts = db.relationship('Cart', back_populates= 'items', cascade = 'all, delete-orphan')
    cart_items = db.relationship('Cart_item', back_populates = "item", cascade = "all, delete-orphan")

    #----------------------association-proxy-----------------------------
    customers = association_proxy('cart_items', 'cart.customer')
    cart = association_proxy('Cart_item', 'cart')
    # ('Cart', 'customer')

    #----------------------serialization---------------------------------
    serialize_rules = ('-bakery.items', '-reviews.items', '-cart_items.item', '-cart_items.cart')

    #----------------------validations-----------------------------------
    @validates('name')
    def validates_name(self, key, name):
        if not name:
            raise ValueError('name cannot be empty!')
        return name


class Customer (db.Model, SerializerMixin):
    __tablename__ = "customers"

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)
    username = db.Column(db.String, unique = True)
    email = db.Column(db.String, unique = True)
    _password_hash = db.Column(db.String)

    #----------------------foreign-keys----------------------------------
    
    #----------------------relationships---------------------------------
    reviews = db.relationship('Review', back_populates = 'customer', cascade = 'all, delete-orphan')
    carts = db.relationship('Cart', back_populates = 'customer', cascade = 'all, delete-orphan')

    #----------------------association-proxy-----------------------------
    items = association_proxy('carts', 'items')
    # items = association_proxy('Cart', 'item')

    #----------------------serialization---------------------------------
    serialize_rules = ('-reviews.customer', '-carts.customer')

    #----------------------validations-----------------------------------
    @validates('name')
    def validates_name(self, key, name):
        if not name:
            raise ValueError('name cannot be empty!')
        return name
    
    @validates('username')
    def validates_username(self, key, username):
        if not username:
            raise ValueError('username cannot be empty!')
        return username
        
    @validates('email')
    def validates_email(self, key, email):
        if not email or '.com' not in email or '@' not in email :
            raise ValueError('Invalid email')
        return email
    

    @hybrid_property
    def password_hash(self):
        raise AttributeError("Don't have permission to access the password")

    @password_hash.setter
    def password_hash(self, password):
        new_password_hash = bcrypt.generate_password_hash(password.encode('utf-8'))
        self._password_hash = new_password_hash.decode('utf-8')

    def authenticate(self, password):
        return bcrypt.check_password_hash(
            self._password_hash, password.encode('utf-8'))


class Review (db.Model, SerializerMixin):
    __tablename__ = "reviews"

    id = db.Column(db.Integer, primary_key = True)
    comment = db.Column(db.String)

    #----------------------foreign-keys----------------------------------
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'))
    item_id = db.Column(db.Integer, db.ForeignKey('items.id'))

    #----------------------relationships---------------------------------
    customer = db.relationship('Customer', back_populates = 'reviews')
    item = db.relationship('Item', back_populates = 'reviews')

    #----------------------association-proxy-----------------------------

    #----------------------serialization---------------------------------
    serialize_rules = ('-customer.reviews', '-item.reviews')


class Cart (db.Model, SerializerMixin):
    __tablename__ = "carts"

    id = db.Column(db.Integer, primary_key = True)

    #----------------------foreign-keys----------------------------------
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'))

    #----------------------relationships---------------------------------
    customer = db.relationship('Customer', back_populates = 'carts')
    cart_items = db.relationship('Cart_item', back_populates = 'cart')
    # items = db.relationship('Item', back_populates = 'carts')

    #----------------------association-proxy-----------------------------
    items = association_proxy("cart_items", "item")

    #----------------------serialization---------------------------------
    serialize_rules = ('-customer.carts', '-cart_items.cart', '-customer.reviews', '-cart_items.item')


class Cart_item (db.Model, SerializerMixin):
    __tablename__ = "cart_items"

    id = db.Column(db.Integer, primary_key = True)
    cart_id = db.Column(db.Integer, db.ForeignKey('carts.id'))
    item_id = db.Column(db.Integer, db.ForeignKey('items.id'))

    #----------------------relationships---------------------------------
    cart = db.relationship('Cart', back_populates = 'cart_items')
    item = db.relationship('Item', back_populates = 'cart_items')
    
    #----------------------association-proxy-----------------------------
    items = association_proxy('item', 'cart')

    #----------------------serialization---------------------------------
    serialize_rules = ('-cart.cart_items', '-item.cart_items', )



class Bakery (db.Model, SerializerMixin):
    __tablename__ = "bakery"

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)
    hours = db.Column(db.Integer)
    # email = db.Column(db.String)
    # password = db.Column(db.String)

    #----------------------foreign-keys----------------------------------

    #----------------------relationships---------------------------------
    items = db.relationship('Item', back_populates = 'bakery', cascade = 'all, delete-orphan')

    #----------------------association-proxy-----------------------------

    #----------------------serialization---------------------------------
    serialize_rules = ('-items.bakery',)