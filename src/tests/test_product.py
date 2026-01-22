from daos.product_dao import ProductDAO
from models.product import Product

dao = ProductDAO()

def test_product_insert(): 
    product = Product(None, "Test Product", "TestBrand", 99.99)
    dao.insert(product)
    products = dao.select_all()
    names = [p.name for p in products]
    assert product.name in names

def test_product_update():
    product = Product(None, "Test Product", "TestBrand", 99.99)
    new_id = dao.insert(product)
    new_name = "Updated Product"
    product.id= new_id
    product.name = new_name
    dao.update(product)

    products = dao.select_all()
    names = [p.name for p in products]
    assert new_name in names

    dao.delete(new_id)
    
def test_product_delete():
    product = Product(None, "Test Product 2", "TestBrand", 99.99)
    product_id = dao.insert(product)
    dao.delete(product_id)

    new_dao = ProductDAO()
    products = new_dao.select_all()
    ids = [p.id for p in products]
    assert product.id not in ids




