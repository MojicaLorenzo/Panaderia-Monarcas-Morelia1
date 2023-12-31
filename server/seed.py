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
                description="wheat flour, water or milk, sugar, butter, eggs, yeast, and salt",
                price=0.75,
                quantity=20,
                image='https://blog.amigofoods.com/wp-content/uploads/2021/01/mexican-sweet-bread-concha.jpg',
                bakery_id= 1,
            ),
            Item(
                name="Sugar Donut",
                type="Sweet",
                description="Milk, Eggs, Sugar, Yeast, Butter, and Flour",
                price=0.75,
                quantity=20,
                image='https://tornadoughalli.com/wp-content/uploads/2022/06/CINNAMON-SUGAR-MINI-DONUTS-2-1.jpg',
                bakery_id= 1,
            ),
            Item(
                name="Cortadillo",
                type="Sweet",
                description="Milk, Eggs, Sugar, Yeast, Butter, and Flour",
                price=1.50,
                quantity=20,
                image='https://www.maricruzavalos.com/wp-content/uploads/2020/11/cortadillos-mexicanos-recipe.jpg',
                bakery_id= 1,
            ),
            Item(
                name="Mantecada",
                type="Sweet",
                description="Flour, Egg, Sugar, and Butter.",
                price=0.75,
                quantity=20,
                image='https://i0.wp.com/chicanoeats.com/wp-content/uploads/2019/03/IMG_6257.jpg?fit=2400%2C2401&ssl=1',
                bakery_id= 1,
            ),
            Item(
                name="Galleta con Gragea",
                type="Sweet",
                description="Flour, Egg, Sugar,flour, baking soda, salt and Butter",
                price=0.75,
                quantity=20,
                image='https://cdn.vox-cdn.com/thumbor/z6Wl338jfISB5gLh0A5g0-yOJHU=/33x0:566x400/1200x900/filters:focal(33x0:566x400)/cdn.vox-cdn.com/uploads/chorus_image/image/51517059/El_Burrito_Mercado_cookies.0.0.png',
                bakery_id= 1,
            ),
            Item(
                name="Polvoron",
                type="Sweet",
                description="cocoa powder, all purpose flour, egg, powdered sugar, shortening, and salt",
                price=0.75,
                quantity=20,
                image='https://mysliceofmexico.files.wordpress.com/2021/12/019-20191126-polvorones-napolitanos.jpg?w=1024',
                bakery_id= 1,
            ),
            Item(
                name="Telera",
                type="Savory",
                description="wheat flour, yeast, water and salt",
                price=0.75,
                quantity=20,
                image='https://blog.elamasadero.com/wp-content/uploads/teleras.jpg',
                bakery_id= 1,
            ),
            Item(
                name="Bolillo",
                type="Savory",
                description="wheat flour, yeast, water and salt",
                price=0.75,
                quantity=20,
                image='https://www.isabeleats.com/wp-content/uploads/2022/12/bolillo-2022-small-15.jpg',
                bakery_id= 1,
            ),
            Item(
                name="Mini Concha",
                type="Sweet",
                description="wheat flour, water or milk, sugar, butter, eggs, yeast, and salt",
                price=0.50,
                quantity=20,
                image='https://i.pinimg.com/736x/82/91/20/8291203fc71e36fcd3f7744236a295cd.jpg',
                bakery_id= 1,
            ),
            Item(
                name="Chocolate Donut",
                type="Sweet",
                description="Milk, Eggs, Sugar, Yeast, Butter, Chocolate, and Flour",
                price=1,
                quantity=20,
                image='https://www.chiselandfork.com/wp-content/uploads/2020/01/chocolate-frosted-donuts-1.jpg',
                bakery_id= 1,
            ),
            Item(
                name="Orejas",
                type="Sweet",
                description="milk, sugar, butter, and eggs",
                price=1.50,
                quantity=20,
                image='https://stellanspice.com/wp-content/uploads/2022/12/A7401740-683x1024.jpg',
                bakery_id= 1,
            ),
            Item(
                name="Sema de trigo",
                type="Savory",
                description="Whole Wheat Flour, Yeast, Salt, and Egg",
                price=1,
                quantity=20,
                image='https://img-global.cpcdn.com/recipes/178a0a40a3824bd6/680x482cq70/pan-marroqui-casero-facil-de-hacer-y-esponjoso-foto-principal.jpg',
                bakery_id= 1,
            ),
            Item(
                name="Niño envuelto",
                type="Sweet",
                description="milk, sugar, butter, and eggs",
                price=1.50,
                quantity=20,
                image='https://endoedibles.com/wp-content/uploads/2018/05/DSC00007.jpg',
                bakery_id= 1,
            ),
            Item(
                name="Empanada de calabaza",
                type="Sweet",
                description="Sugar, Water, Yeast, Egg, Vegetable Shortening, Pumpkin, and Cinnamon",
                price=2,
                quantity=20,
                image='https://www.goya.com/media/4231/pumpkin-hand-pies1.jpg?quality=80',
                bakery_id= 1,
            ),
            Item(
                name="Cono relleno",
                type="Sweet",
                description="Flour, Milk, Sugar, Butter, Eggs,",
                price=2,
                quantity=20,
                image='https://static.wixstatic.com/media/758c73_dc3db536025c45b4bfdb2cd44d514cfc~mv2.jpg/v1/fill/w_1000,h_800,al_c,q_85,usm_0.66_1.00_0.01/758c73_dc3db536025c45b4bfdb2cd44d514cfc~mv2.jpg',
                bakery_id= 1,
            ),
            Item(
                name="Elote Fino",
                type="Sweet",
                description="Yeast, Cinnamon, Eggs, Unsalted Butter, and Milk",
                price=0.75,
                quantity=20,
                image='https://i.ytimg.com/vi/ILVv8WdbyFU/maxresdefault.jpg',
                bakery_id= 1,
            ),
            Item(
                name="Concha de Chocolate",
                type="Sweet",
                description="Wheat flour, Milk, Sugar, Butter, Eggs, Yeast, Cocoa Powder and salt",
                price=0.75,
                quantity=20,
                image='https://images.squarespace-cdn.com/content/v1/6005e21b6f0b7e66aaa7b908/1634007766364-1UMSVBAQNN1ZSK57HZ5Z/Concha+de+Chocolate_104.jpg',
                bakery_id= 1,
            ),
            Item(
                name="Puerquitos",
                type="Sweet",
                description="Flour, Eggs, Molasses, Milk, Salt, and Butter",
                price=0.75,
                quantity=20,
                image='https://animalgourmet.com/wp-content/uploads/2020/04/puerquitos-piloncillo.jpg',
                bakery_id= 1,
            ),
            Item(
                name="Cuerno",
                type="Sweet",
                description="Eggs, Baking powder, All-purpose shortening, Pastry flour, and Powdered sugar",
                price=0.75,
                quantity=20,
                image='https://www.bakemag.com/-/media/125DEE083ABA4318BC12E0BE29320FAC.ashx',
                bakery_id= 1,
            ),
            Item(
                name="Churro",
                type="Sweet",
                description="Water, Sugar, Salt, Vegetable Oil, Flour, and Cinnamon",
                price=1.50,
                quantity=20,
                image='https://www.jessicagavin.com/wp-content/uploads/2020/04/churros-13-1200.jpg',
                bakery_id= 1,
            ),
            Item(
                name="Strawberry Donut",
                type="Sweet",
                description="Milk, Eggs, Sugar, Yeast, Butter, and Flour",
                price=0.75,
                quantity=20,
                image='https://funcakes.com/content/uploads/2020/08/Donut-1000x750.png',
                bakery_id= 1,
            ),
]

            
            db.session.add_all(items)

            db.session.commit()

    # def seed_customers():
    #         customers = [
    #         Customer(
    #             name="enzo",
    #             username="enzo",
    #             email="example@example.com",
    #             _password_hash="password",
    #         )
    #     ]
    #         db.session.add_all(customers)

    #         db.session.commit()
    
    # def seed_reviews():
    #         reviews = [
    #         Review(
    #         comment = "Super duper delicious 10/10",
    #         customer_id = 1,
    #         item_id = 1,
    #         ),
    #         Review(
    #             comment = "Yummy wummy",
    #             customer_id = 2,
    #             item_id = 3
    #         )
    #     ]
    #         db.session.add_all(reviews)

    #         db.session.commit()

    def seed_bakery():
            bakery = Bakery(
                name="Panaderia Monarcas Morelia",
                hours = 3,
            )
            db.session.add(bakery)

            db.session.commit()

    # def seed_carts():
    #         carts = [
    #         Cart(
    #         customer_id = 1,
    #         )
    #     ]

    #         db.session.add_all(carts)

    #         db.session.commit()
    
    # def seed_cart_items():
    #         cart_items = [
    #         Cart_item(
    #             item_id = 1,
    #             cart_id = 1
    #         ),
    #         Cart_item(
    #             item_id = 2,
    #             cart_id = 1
    #         )
    #     ]
    #         db.session.add_all(cart_items)

    #         db.session.commit()

    if __name__ == '__main__':
        with app.app_context():
            seed_items() 
            # seed_customers()  
            # seed_reviews()
            seed_bakery()
            # seed_carts()
            # seed_cart_items()

        print('Data has been seeded.')
