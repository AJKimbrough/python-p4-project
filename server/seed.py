#!/usr/bin/env python3

# Standard library imports
from random import randint, choice as rc
import random

# Remote library imports
from faker import Faker

# Local imports
from app import app
from models import db, User, Product, Order, OrderItem

fake = Faker()

def seed_data():
    with app.app_context():
        print("Starting seed...")

        create_users()
        create_products()
        create_orders()
        create_order_items()

        db.session.commit()
        print("Seed completed successfully.")

def create_users():
    users = []
    for i in range(10):
        user = User(
            name = fake.name(),
            email = fake.email(),
            has_account = random.choice([True, False]),
        )

        users.append(user)
    db.session.add_all(users)

def create_products():
    products = []
    for i in range(25):
        product = Product(
            name = fake.name(),
            img = fake.image_url(),
            description = fake.text(),
            price = fake.random_float(),
            quantity = fake.random_int(min=1, max=100),
            in_stock = random.choice([True, False]),

        )

        products.append(product)
    db.session.add_all(products)

def create_orders():
    orders = []
    for i in range(10):
        order = Order(
            order_number = fake.random_int(),
            date = fake.date(),
            ship = random.choice([True, False]),
        )

        orders.append(order)
    db.session.add_all(orders)

def create_order_items():
    order_items = []
    for i in range(30):
        order_item = OrderItem(
            quantity = fake.random_int(min=1, max=10),
        )

        order_items.append(order_item)
    db.session.add_all(order_items)

if __name__ == '__main__':
    seed_data()
