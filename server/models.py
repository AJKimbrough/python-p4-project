from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.ext.hybrid import hybrid_property
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

from config import db

# Models go here!

class User(db.Model, SerializerMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String)
    has_account = db.Column(db.Boolean)
    #_password_hash = db.Column(db.String)

    #@hybrid_property
   # def password_hash(self):
        #if not self._password_hash:
         #   raise Exception('Password hahsed may not be viewed.')
        #return self._password_hash
    
    #@password_hash.setter
    #def password_hash(self, password):
        #password_hash = bcrypt.generate_password_hash(
            #password.encode('utf-8'))
        #self._password_hash = password_hash.decode('utf-8')

    #def authenticate(self, password):
        #return bcrypt.check_password_hash(
            #self._password_hash, password.encode('utf-8'))

    order = db.relationship('Order', backref='user')
    #order_items = db.relationship('OrderItems', backref='users')

    def __repr__(self):
        pass

class Product(db.Model, SerializerMixin):
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    img = db.Column(db.String)
    description = db.Column(db.String)
    price = db.Column(db.Float)
    quantity = db.Column(db.Integer)
    in_stock = db.Column(db.Boolean)

    #order = db.relationship('Order', backref='product')
    orders = db.relationship('Order', backref='customer', foreign_keys='Order.user_id')

    def __repr__(self):
        pass

class Order(db.Model, SerializerMixin):
    __tablename__ = 'orders'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    order_number = db.Column(db.Integer)
    date = db.Column(db.DateTime, server_default=db.func.now())
    shipped = db.Column(db.Boolean, server_default=db.false())

    user = db.relationship('User', backref='order')
    order_items = db.relationship('OrderItem', backref='order')
    

    def __repr__(self):
        pass

class OrderItem(db.Model, SerializerMixin):
    __tablename__ = 'order_items'

    id = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.Integer)

    order = db.relationship('Order', backref='order_item')
    product = db.relationship('Product', backref='order_item')

    def __repr__(self):
        pass
