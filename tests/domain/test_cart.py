import pytest

from my_cake_shop.domain.cart.models import Cart, Product, Price


@pytest.fixture
def my_cart():
    return Cart()


@pytest.fixture
def my_filled_cart(my_cart):
    apple_product = Product(name="Apple Pencil", price=Price(amount=1))
    sonny_product = Product(name="Sony Wireless headphone", price=Price(amount=1))
    my_cart.add(apple_product)
    my_cart.add(sonny_product)
    my_cart.add(apple_product)

    return my_cart, apple_product, sonny_product


def test_cart_is_initialised_with_empty_products_dict(my_cart):
    assert not my_cart.products


def test_cart_equality(my_cart):
    other_cart = Cart()

    assert my_cart == my_cart
    assert my_cart != other_cart


def test_cart_adds_item_to_products(my_cart):
    test_product = Product(name="An awesome product", price=Price(amount=1))

    my_cart.add(test_product)

    assert len(my_cart.products) == 1
    assert test_product in my_cart.products.keys()


def test_cart_adds_specific_product_and_computes_quantity_of_products(my_filled_cart):
    my_cart, apple_product, sonny_product = my_filled_cart

    assert len(my_cart.products) == 2
    assert my_cart.products[apple_product] == 2
    assert my_cart.products[sonny_product] == 1


def test_cart_deletes_specific_product_and_returns_deleted_products(my_filled_cart):
    my_cart, apple_product, sonny_product = my_filled_cart

    my_cart.delete(apple_product)

    assert len(my_cart.products) == 1
    assert len(my_cart.deleted_products) == 1
    assert apple_product in my_cart.deleted_products


def test_cart_checkout(my_filled_cart):
    my_cart, apple_product, sonny_product = my_filled_cart

    flatten_products = my_cart.checkout()

    assert len(flatten_products) == 3
