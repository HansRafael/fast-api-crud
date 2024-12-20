from fastapi import HTTPException
import pytest
from sqlalchemy.orm import Session

from models.product import Product
from module.product_module import create_new_product, delete_product_by_id, get_all_products, update_product_by_id
from schemas.product_schema import ProductCreate, ProductUpdate


@pytest.fixture
def mock_db(mocker):
    return mocker.Mock(spec=Session)

def test_get_all_products(mock_db):
    mock_db.query.return_value.all.return_value = [Product(id=1, name="Test Product")]
    result = get_all_products(mock_db)

    assert len(result) == 1
    assert result[0].name == "Test Product"
    mock_db.query.assert_called_once_with(Product)
    mock_db.query.return_value.all.assert_called_once()

def test_create_new_product(mock_db):
    product_create = ProductCreate(name="New Product", description="Description", price=10.0)
    mock_db.add.return_value = None
    mock_db.commit.return_value = None
    mock_db.refresh.return_value = None
    result = create_new_product(mock_db, product_create)

    assert isinstance(result, Product)
    assert result.name == "New Product"
    mock_db.add.assert_called_once()
    mock_db.commit.assert_called_once()
    mock_db.refresh.assert_called_once()

def test_delete_product_by_id_success(mock_db):
    mock_product = Product(id=1, name="Test Product")
    mock_db.query.return_value.filter.return_value.first.return_value = mock_product

    result = delete_product_by_id(mock_db, 1)

    assert result == {"message": "Product deleted"}
    mock_db.delete.assert_called_once_with(mock_product)
    mock_db.commit.assert_called_once()

def test_delete_product_by_id_not_found(mock_db):
    mock_db.query.return_value.filter.return_value.first.return_value = None

    with pytest.raises(HTTPException) as exc_info:
        delete_product_by_id(mock_db, 1)
    assert exc_info.value.status_code == 404
    assert exc_info.value.detail == "Product not found"

def test_update_product_by_id_success(mock_db):
    mock_product = Product(id=1, name="Old Name", description="Old Description", price=5.0)
    mock_db.query.return_value.filter.return_value.first.return_value = mock_product
    product_update = ProductUpdate(name="New Name", price=10.0)
    result = update_product_by_id(mock_db, 1, product_update)

    assert result.name == "New Name"
    assert result.description == "Old Description"
    assert result.price == 10.0
    mock_db.commit.assert_called_once()
    mock_db.refresh.assert_called_once_with(mock_product)

def test_update_product_by_id_not_found(mock_db):
    mock_db.query.return_value.filter.return_value.first.return_value = None
    product_update = ProductUpdate(name="New Name")

    with pytest.raises(HTTPException) as exc_info:
        update_product_by_id(mock_db, 1, product_update)
    assert exc_info.value.status_code == 404
    assert exc_info.value.detail == "Product not found"