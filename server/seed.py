#!/usr/bin/env python3

# Standard library imports
from random import randint, choice as rc

# Remote library imports
from faker import Faker

# Local imports
from app import app
from models import db, Item, Customer, Review, Cart, Bakery, Cart_item

with app.app_context():

    Item.query.delete()
    Customer.query.delete()
    Review.query.delete()
    Cart.query.delete()
    Bakery.query.delete()
    Cart_item.query.delete()

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
                image='https://blog.amigofoods.com/wp-content/uploads/2021/01/mexican-sweet-bread-concha.jpg',
                bakery_id= 1,
            ),
            Item(
                name="Sugar Donut",
                type="Sweet",
                description="Dead by Daylight is a multiplayer (4vs1) horror game where one player takes on the role of the savage Killer, and the other four players play as Survivors, trying to escape the Killer and avoid being caught and killed.",
                price=20,
                quantity=20,
                image='https://tornadoughalli.com/wp-content/uploads/2022/06/CINNAMON-SUGAR-MINI-DONUTS-2-1.jpg',
                bakery_id= 1,
            ),
            Item(
                name="Cortadillos",
                type="Sweet",
                description="THE NEW FANTASY ACTION RPG. Rise, Tarnished, and be guided by grace to brandish the power of the Elden Ring and become an Elden Lord in the Lands Between.",
                price=60,
                quantity=20,
                image='https://www.maricruzavalos.com/wp-content/uploads/2020/11/cortadillos-mexicanos-recipe.jpg',
                bakery_id= 1,
            ),
            Item(
                name="Mantecadas",
                type="Sweet",
                description="THE NEW FANTASY ACTION RPG. Rise, Tarnished, and be guided by grace to brandish the power of the Elden Ring and become an Elden Lord in the Lands Between.",
                price=60,
                quantity=20,
                image='https://i0.wp.com/chicanoeats.com/wp-content/uploads/2019/03/IMG_6257.jpg?fit=2400%2C2401&ssl=1',
                bakery_id= 1,
            ),
            Item(
                name="Galleta con Gragea",
                type="Sweet",
                description="THE NEW FANTASY ACTION RPG. Rise, Tarnished, and be guided by grace to brandish the power of the Elden Ring and become an Elden Lord in the Lands Between.",
                price=60,
                quantity=20,
                image='https://cdn.vox-cdn.com/thumbor/z6Wl338jfISB5gLh0A5g0-yOJHU=/33x0:566x400/1200x900/filters:focal(33x0:566x400)/cdn.vox-cdn.com/uploads/chorus_image/image/51517059/El_Burrito_Mercado_cookies.0.0.png',
                bakery_id= 1,
            ),
            Item(
                name="Polvoron",
                type="savory",
                description="THE NEW FANTASY ACTION RPG. Rise, Tarnished, and be guided by grace to brandish the power of the Elden Ring and become an Elden Lord in the Lands Between.",
                price=60,
                quantity=20,
                image='https://mysliceofmexico.files.wordpress.com/2021/12/019-20191126-polvorones-napolitanos.jpg?w=1024',
                bakery_id= 1,
            )
]

            
            db.session.add_all(items)

            db.session.commit()

    def seed_customers():
            customers = [
            Customer(
                name="enzo",
                username="enzo",
                email="example@example.com",
                _password_hash="password",
            ),
            Customer(
                name="bob",
                username="bob",
                email="bob@example.com",
                _password_hash="bob",
            )
        ]
            db.session.add_all(customers)

            db.session.commit()
    
    def seed_reviews():
            reviews = [
            Review(
            comment = "Super duper delicious 10/10",
            customer_id = 1,
            item_id = 1,
            ),
            Review(
                comment = "Yummy wummy",
                customer_id = 2,
                item_id = 3
            )
        ]
            db.session.add_all(reviews)

            db.session.commit()

    def seed_bakery():
            bakery = Bakery(
                name="Panaderia Monarcas Morelia",
                hours = 3,
            )
            db.session.add(bakery)

            db.session.commit()

    def seed_carts():
            carts = [
            Cart(
            customer_id = 1,
            ),
            Cart(
            customer_id = 1,
            )
        ]

            db.session.add_all(carts)

            db.session.commit()
    
    def seed_cart_items():
            cart_items = [
            Cart_item(
                item_id = 1,
                cart_id = 1
            ),
            Cart_item(
                item_id = 2,
                cart_id = 1
            )
        ]
            db.session.add_all(cart_items)

            db.session.commit()

    if __name__ == '__main__':
        with app.app_context():
            seed_items() 
            seed_customers()  
            seed_reviews()
            seed_bakery()
            seed_carts()
            seed_cart_items()

        print('Data has been seeded.')
