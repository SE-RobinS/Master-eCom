# models/product.py
from utils.firebase import db

class Product:
    def __init__(self):
        self.collection = db.collection('products')

    def add_product(self, product_data):
        return self.collection.add(product_data).id

    def get_all_products(self):
        return [doc.to_dict() for doc in self.collection.stream()]