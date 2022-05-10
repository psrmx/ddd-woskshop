from collections import defaultdict
from pydantic import BaseModel


class Product(BaseModel):
    name: str

    class Config:
        allow_mutation = False

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other):
        if self.name == other.name:
            return True
        return False


class Cart(BaseModel):
    products: dict[Product, int] = defaultdict(int)
    deleted_products: list[Product] = []

    def add(self, product: Product):
        self.products[product] += 1

    def delete(self, product: Product):
        self.products.pop(product)
        self.deleted_products.append(product)
