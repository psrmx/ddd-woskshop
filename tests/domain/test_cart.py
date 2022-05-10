import pytest
from my_cake_shop.domain.models import Cart, Product


@pytest.fixture
def my_cart():
    return Cart()


def test_cart_is_initialised_with_empty_products_dict(my_cart):
    assert not my_cart.products


def test_cart_adds_item_to_products(my_cart):
    test_product = Product(name="An awesome product")

    my_cart.add(test_product)

    assert len(my_cart.products) == 1
    assert test_product in my_cart.products.keys()


def test_cart_adds_specific_product_and_computes_quantity_of_products(my_cart):
    apple_product = Product(name="Apple Pencil")
    sonny_product = Product(name="Sony Wireless headphone")

    my_cart.add(apple_product)
    my_cart.add(sonny_product)
    my_cart.add(apple_product)

    assert len(my_cart.products) == 2
    assert my_cart.products[apple_product] == 2
    assert my_cart.products[sonny_product] == 1


def test_cart_deletes_specific_product_and_returns_deleted_products(my_cart):
    apple_product = Product(name="Apple Pencil")
    sonny_product = Product(name="Sony Wireless headphone")

    my_cart.add(apple_product)
    my_cart.add(sonny_product)
    my_cart.add(apple_product)
    my_cart.delete(apple_product)

    assert len(my_cart.products) == 1
    assert len(my_cart.deleted_products) == 1
    assert apple_product in my_cart.deleted_products


def test_cart_equality(my_cart):
    other_cart = Cart()

    assert my_cart == my_cart
    assert my_cart != other_cart
