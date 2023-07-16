from db import db
from models.Product import Product
from flask_marshmallow import Marshmallow

ma = Marshmallow()

class ProductService:
    def create_product(self, name:str) -> Product:
        new_product = Product(name)
        db.session.add(new_product)
        db.session.commit()
        return new_product
    
    def list_products(self) ->list:
        return db.session.execute(db.select(Product).order_by(Product.name)).scalars()
    
    def find_by_id(self, id:int) -> Product:
        return db.session.get(Product,id)
    
    def update(self, id:int, name:str)->Product:
        update_product:Product = db.session.get(Product,id)
        update_product.name = name
        db.session.add(update_product)
        db.session.commit()
        return update_product
    
    def delete(self,id:int) ->Product:
        delete_product:Product = db.session.get(Product,id)
        db.session.delete(delete_product)
        db.session.commit()
        return delete_product

class Product_schema(ma.Schema):
    class Meta:
        fields = ('id','name')

products_schema = Product_schema(many=True)
product_schema = Product_schema()
