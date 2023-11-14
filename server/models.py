from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.orm import validates
import re
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})
db = SQLAlchemy(metadata=metadata)

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
    reviews = db.relationship('Review', back_populates = 'items', cascade = 'all, delete-orphan')
    carts = db.relationship('Item', back_populates= 'items', cascade = 'all, delete-orphan')

    # association proxy
    customers = association_proxy('Cart', 'customer')

    # serialization
    serialize_rules = ('-bakery.items', '-reviews.items', '-carts.items')

    #validation


class Customer (db.Model, SerializerMixin):
    __tablename__ = "customers"

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)
    username = db.Column(db.String, unique = True)
    email = db.Column(db.String)
    password = db.Column(db.String)

    # foreign keys
    
    # relationships
    reviews = db.relationship('Review', back_populates = 'customer', cascade = 'all, delete-orphan')
    carts = db.relationship('Cart', back_populates = 'customer', cascade = 'all, delete-orphan')

    # association proxy
    items = association_proxy('Cart', 'item')

    # serialization
    serialize_rules = ('-reviews.customer', '-carts.customer')


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
    item = db.relationship('Item', back_populates = 'carts')

    # association proxy

    # serialization
    serialize_rules = ('-customer, carts', '-item.carts')


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