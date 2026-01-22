import pytest
from daos.product_dao import ProductDAO
from models.product import Product

@pytest.fixture(scope="module")
def dao():
    dao_instance = ProductDAO()
    yield dao_instance
    dao_instance.delete_all()  # Cleanup après tous les tests
    dao_instance.close()

@pytest.fixture
def sample_product():
    return Product(None, "Test Product", "TestBrand", 99.99)

def test_product_select(dao, sample_product):  # <-- dao et sample_product en arguments
    dao.insert(sample_product)
    products = dao.select_all()
    names = [p.name for p in products]
    assert sample_product.name in names

def test_product_insert(dao, sample_product):
    product_id = dao.insert(sample_product)
    assert isinstance(product_id, int) and product_id > 0

def test_product_update(dao, sample_product):
    product_id = dao.insert(sample_product)
    sample_product.id = product_id
    sample_product.name = "Updated Product"
    sample_product.brand = "UpdatedBrand"
    sample_product.price = 199.99
    rows_modified = dao.update(sample_product)
    assert rows_modified == 1

    products = dao.select_all()
    updated_names = [p.name for p in products]
    assert "Updated Product" in updated_names

def test_product_delete(dao, sample_product):
    product_id = dao.insert(sample_product)
    rows_deleted = dao.delete(product_id)
    assert rows_deleted == 1

    products = dao.select_all()
    names = [p.name for p in products]
    assert sample_product.name not in names
