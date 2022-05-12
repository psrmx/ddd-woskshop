import decimal
from dataclasses import dataclass, field
from moneyed import Currency, USD


@dataclass(frozen=True)
class PriceDTO:
    amount: decimal
    currency: Currency = field(default=USD)


@dataclass
class ProductDTO:
    name: str
    price: PriceDTO
