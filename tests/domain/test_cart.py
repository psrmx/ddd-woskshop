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


def test_cart_adds_specific_items_and_computes_quantity_of_products(my_cart):
    apple_product = Product(name="Apple Pencil")
    sonny_product = Product(name="Sony Wireless headphone")

    my_cart.add(apple_product)
    my_cart.add(sonny_product)
    my_cart.add(apple_product)

    assert len(my_cart.products) == 2
    assert my_cart.products[apple_product] == 2
    assert my_cart.products[sonny_product] == 1
