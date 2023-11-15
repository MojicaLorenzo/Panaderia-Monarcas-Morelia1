#!/usr/bin/env python3

# Standard library imports
from random import randint, choice as rc

# Remote library imports
from faker import Faker

# Local imports
from app import app
from models import db, Item, Customer, Review, Cart, Bakery

with app.app_context():

    Item.query.delete()
    Customer.query.delete()
    Review.query.delete()
    Cart.query.delete()
    Bakery.query.delete()

    db.session.commit()


    fake = Faker()

    def seed_items():
            items = [
            Item(
                name="Concha",
                type="Sweet",
                description="Apex Legends is the award-winning, free-to-play Hero Shooter from Respawn Entertainment. Master an ever-growing roster of legendary characters with powerful abilities, and experience strategic squad play and innovative gameplay in the next evolution of Hero Shooter and Battle Royale.",
                price=30,
                quantity=20,
                image='https://media.contentapi.ea.com/content/dam/apex-legends/images/2020/10/champion-edition/apex-champion-edittion-featured-image.jpg.adapt.crop191x100.628p.jpg',
                bakery_id= 1,
            ),
            Item(
                name="Sugar Donut",
                type="Sweet",
                description="Dead by Daylight is a multiplayer (4vs1) horror game where one player takes on the role of the savage Killer, and the other four players play as Survivors, trying to escape the Killer and avoid being caught and killed.",
                price=20,
                quantity=20,
                image='https://cdn1.epicgames.com/offer/611482b8586142cda48a0786eb8a127c/EGS_DeadbyDaylight_BehaviourInteractive_S1_2560x1440-a32581cf9948a9a2e24b2ff15c1577c7',
                bakery_id= 1,
            ),
            Item(
                name="Bolillo",
                type="Savory",
                description="THE NEW FANTASY ACTION RPG. Rise, Tarnished, and be guided by grace to brandish the power of the Elden Ring and become an Elden Lord in the Lands Between.",
                price=60,
                quantity=20,
                image='https://image.api.playstation.com/vulcan/ap/rnd/202110/2000/aGhopp3MHppi7kooGE2Dtt8C.png',
                bakery_id= 1,
            )
]

            
            db.session.add_all(items)

            db.session.commit()

    def seed_customers():
            customer = Customer(
                name="enzo",
                username="enzowenzo",
                email="example@example.com",
                password_hash="apple561",
            )
            db.session.add(customer)

            db.session.commit()
    
    def seed_reviews():
            review = Review(
            comment = "Super duper delicious 10/10",
            customer_id = 1,
            item_id = 1,
            )

            db.session.add(review)

            db.session.commit()

    def seed_bakery():
            bakery = Bakery(
                name="Panaderia Monarcas Morelia",
                hours = 3,
            )
            db.session.add(bakery)

            db.session.commit()

    def seed_carts():
            cart = Cart(
                customer_id = 1,
                item_id = 2
            )
            db.session.add(cart)

            db.session.commit()

    if __name__ == '__main__':
        with app.app_context():
            seed_items()  
            seed_customers()  
            seed_reviews()
            seed_bakery()
            seed_carts()

        print('Data has been seeded.')
