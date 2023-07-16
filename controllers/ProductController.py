from flask import request,Blueprint,jsonify
from service.ProductService import *

product = Blueprint('product',__name__)
product_serv = ProductService()

@product.route('/product/new', methods=['POST'])
def create_product():
    return product_schema.jsonify(product_serv.create_product(request.json['name']))

@product.route('/product/list/all', methods=['GET'])
def list_products():
    return products_schema.jsonify(product_serv.list_products())

@product.route('/product', methods=['GET'])
def find_by_id():
    return product_schema.jsonify(product_serv.find_by_id(request.args.get('id')))

@product.route('/product/update', methods=['PUT'])
def update():
    id = request.json['id']
    name = request.json['name']
    return product_schema.jsonify(product_serv.update(id,name))

@product.route('/product/delete', methods=['DELETE'])
def delete():
    return product_schema.jsonify(product_serv.delete(request.args.get('id')))

