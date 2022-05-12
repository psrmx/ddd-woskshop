from my_cake_shop.domain.order.models import Order, Product, Price
from moneyed import USD


apple_product = Product(name="Apple Pencil", price=Price(amount=1), weight=100)
sonny_product = Product(name="Sony Wireless headphone", price=Price(amount=1), weight=200)


def test_total_cost_of_order():
    flatten_products_in_cart = [
        Product(name="Apple Pencil", price=Price(amount=1), weight=100),
        Product(name="Sony Wireless headphone", price=Price(amount=1), weight=200),
        Product(name="Apple Pencil", price=Price(amount=1), weight=100)
    ]
    my_order = Order(flatten_products_in_cart)

    actual_total = my_order.calculate_total_cost()

    expected_total = Price(amount=43, currency=USD)
    assert actual_total == expected_total
