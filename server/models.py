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

    # foreign keys
    bakery_id = db.Column(db.Integer, db.ForeignKey('bakery.id'))

    # relationships
    bakery = db.relationship('Bakery', back_populates = 'items')
    reviews = db.relationship('Review', back_populates = 'item', cascade = 'all, delete-orphan')
    carts = db.relationship('Cart', back_populates= 'items', cascade = 'all, delete-orphan')

    # association proxy
    customers = association_proxy('Cart', 'customer')

    # serialization
    serialize_rules = ('-bakery.items', '-reviews.items', '-carts.items')

    #validation
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
    password_hash = db.Column(db.String, nullable = False)

    # foreign keys
    
    # relationships
    reviews = db.relationship('Review', back_populates = 'customer', cascade = 'all, delete-orphan')
    carts = db.relationship('Cart', back_populates = 'customer', cascade = 'all, delete-orphan')

    # association proxy
    items = association_proxy('Cart', 'item')

    # serialization
    serialize_rules = ('-reviews.customer', '-carts.customer')

    #validations
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
        
    def set_password(self, password):
        self.password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)
        
        # move to front-end
    # @validates('password_hash')
    # def validates_password_hash(self, key, password_hash):
    #     if len(password_hash) < 8:
    #         raise ValueError("Make sure your password is at lest 8 letters")
    #     elif re.search('[0-9]',password_hash) is None:
    #         raise ValueError("Make sure your password has a number in it")
    #     elif re.search('[A-Z]',password_hash) is None: 
    #         raise ValueError("Make sure your password has a capital letter in it")
    #     else:
    #         return password_hash


class Review (db.Model, SerializerMixin):
    __tablename__ = "reviews"

    id = db.Column(db.Integer, primary_key = True)
    comment = db.Column(db.String)

    # foreign keys
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'))
    item_id = db.Column(db.Integer, db.ForeignKey('items.id'))

    # relationships
    customer = db.relationship('Customer', back_populates = 'reviews')
    item = db.relationship('Item', back_populates = 'reviews')

    # association proxy

    # serialization
    serialize_rules = ('-customer.reviews', '-item.reviews')


class Cart (db.Model, SerializerMixin):
    __tablename__ = "carts"

    id = db.Column(db.Integer, primary_key = True)

    # foreign keys
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'))
    item_id = db.Column(db.Integer, db.ForeignKey('items.id'))

    # relationships
    customer = db.relationship('Customer', back_populates = 'carts')
    items = db.relationship('Item', back_populates = 'carts')

    # association proxy

    # serialization
    serialize_rules = ('-customer.carts', '-item.carts')


class Bakery (db.Model, SerializerMixin):
    __tablename__ = "bakery"

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)
    hours = db.Column(db.Integer)
    # email = db.Column(db.String)
    # password = db.Column(db.String)

    # foreign keys

    # relationships
    items = db.relationship('Item', back_populates = 'bakery', cascade = 'all, delete-orphan')

    # association proxy

    # serialization
    serialize_rules = ('-items.bakery',)