from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.ext.hybrid import hybrid_property


from config import db, bcrypt

# Models go here!

class User(db.Model, SerializerMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String)
    has_account = db.Column(db.Boolean)
    _password_hash = db.Column(db.String)

    @hybrid_property
    def password_hash(self):
        if not self._password_hash:
            raise Exception('Password hahsed may not be viewed.')
        return self._password_hash
    
    @password_hash.setter
    def password_hash(self, password):
        password_hash = bcrypt.generate_password_hash(
            password.encode('utf-8'))
        self._password_hash = password_hash.decode('utf-8')

    def authenticate(self, password):
        return bcrypt.check_password_hash(
            self._password_hash, password.encode('utf-8'))

    order = db.relationship('Order', backref='user')
    #order_items = db.relationship('OrderItems', backref='users')

    def __repr__(self):
        pass

class Product(db.Model, SerializerMixin):
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    price = db.Column(db.Float)
    quantity = db.Column(db.Integer)
    in_stock = db.Column(db.Boolean)

    order = db.relationship('Order', backref='product')

    def __repr__(self):
        pass

class Order(db.Model, SerializerMixin):
    __tablename__ = 'orders'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, server_default=db.func.now())
    shipped = db.Column(db.Boolean)

    user = db.relationship('User', backref='orders')
    order_items = db.relationship('OrderItems', backref='order')

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
