from fastapi import FastAPI

from my_cake_shop.domain.models import Cart, Product, Price

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello and welcome to our cake shop!"}


@app.get("/cart")
def add_cart_product():
    cart = Cart()
    apple_pencil_product = Product(name="Apple Pencil", price=Price(amount=1))
    sonny_product = Product(name="Sony Wireless headphone", price=Price(amount=1))
    cart.add(apple_pencil_product)
    cart.add(sonny_product)
    cart.add(apple_pencil_product)
    cart.delete(apple_pencil_product)
    my_order = cart.checkout()
    return {
        "products": cart.products.__str__(),
        "deleted_products": cart.deleted_products,
        "order": my_order,
    }
