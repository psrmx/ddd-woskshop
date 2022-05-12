import decimal

from dataclasses import dataclass, field
from moneyed import Currency, USD
from my_cake_shop.common.dtos import ProductDTO


@dataclass(frozen=True)
class Price:
    amount: decimal
    currency: Currency = field(default=USD)

    def add(self, other):
        new_amount = self.amount + other.amount
        return Price(amount=new_amount, currency=USD)


@dataclass(frozen=True)
class Product:
    name: str
    price: Price
    weight: float


@dataclass
class Order:
    products: list[Product] = field(default_factory=list)

    def calculate_total_cost(self) -> Price:
        total_cost: Price = Price(amount=0, currency=USD)
        total_weight: float = 0
        for product in self.products:
            total_cost = total_cost.add(product.price)
            total_weight += product.weight

        total_cost = total_cost.add(Price(amount=total_weight*0.1, currency=USD))
        return total_cost
