# Fortsättning på app.py
from flask import Flask, jsonify, request
from models.product import Product

app = Flask(__name__)
product_model = Product()

@app.route('/products', methods=['GET'])
def get_products():
    products = product_model.get_all_products()
    return jsonify(products)

@app.route('/products', methods=['POST'])
def add_product():
    product_data = request.json
    product_id = product_model.add_product(product_data)
    return jsonify({"product_id": product_id}), 201

if __name__ == '__main__':
    app.run(debug=True)
