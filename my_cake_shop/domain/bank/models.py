from dataclasses import dataclass, field
from uuid import uuid4, UUID


@dataclass(frozen=True)
class Address:
    city: str


@dataclass
class Account:
    account_id: UUID = field(init=False, default_factory=uuid4)
    address: Address

    def update_address(self, new_address: Address):
        self.address = new_address


@dataclass
class Customer:
    customer_id: UUID = field(init=False, default_factory=uuid4)
    address: Address
    accounts: list[Account] = field(default_factory=list)

    def update_address(self, new_address: Address):
        self.address = new_address
        for account in self.accounts:
            account.update_address(new_address)


def main():
    old_address = Address("Berlin")
    customer = Customer(old_address, accounts=[Account(old_address), Account(old_address)])
    print(customer)

    new_address = Address("Mannheim")
    customer.update_address(new_address)
    print(customer)


if __name__ == '__main__':
    main()
