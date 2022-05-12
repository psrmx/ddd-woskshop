from fastapi import FastAPI

from my_cake_shop.domain.cart.models import Cart, Product as CartProduct, Price
from my_cake_shop.domain.order.models import Order, Product as OrderProduct

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello and welcome to our cake shop!"}


@app.get("/cart")
def add_cart_product():
    cart = Cart()
    apple_pencil_product = CartProduct(name="Apple Pencil", price=Price(amount=1))
    sonny_product = CartProduct(name="Sony Wireless headphone", price=Price(amount=1))

    cart.add(apple_pencil_product)
    cart.add(sonny_product)
    cart.add(apple_pencil_product)
    cart.delete(apple_pencil_product)
    cart_products = cart.checkout()

    weights_of_products = dict([("Apple Pencil", 100), ("Sony Wireless headphone", 200)])
    order_products = [
        OrderProduct(
            product.name,
            product.price,
            weights_of_products[product.name]
        ) for product in cart_products]
    my_order = Order(order_products)
    total_cost = my_order.calculate_total_cost()

    return {
        "products": cart.products.__str__(),
        "deleted_products": cart.deleted_products,
        "order": my_order,
        "total_cost": total_cost
    }
