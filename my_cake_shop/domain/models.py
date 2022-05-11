import decimal
from collections import defaultdict
from dataclasses import dataclass, field

from moneyed import Currency, USD


@dataclass(frozen=True)
class Price:
    amount: decimal
    currency: Currency = field(default=USD)

    def discounted_by(self, percentage: decimal):
        return self.amount * (1 - percentage)


@dataclass(frozen=True)
class Product:
    name: str
    price: Price


@dataclass
class Cart:
    products: dict[Product, int] = field(default_factory=lambda: defaultdict(int))
    deleted_products: list[Product] = field(default_factory=list)
    is_checkout: bool = field(default=False, init=False)

    def add(self, product: Product):
        self.products[product] += 1

    def delete(self, product: Product):
        self.products.pop(product)
        self.deleted_products.append(product)

    def checkout(self):
        self.is_checkout = True

        order_products = []
        for product, quantity in self.products.items():
            order_products.extend([product] * quantity)

        return Order(products=order_products)

    def __eq__(self, other):
        return self is other


@dataclass
class Order:
    products: list[Product] = field(default_factory=list)
