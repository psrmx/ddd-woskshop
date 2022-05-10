from fastapi import FastAPI
from my_cake_shop.domain.models import Cart, Product


app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello and welcome to our cake shop!"}


@app.get("/cart")
def add_cart_product():
    cart = Cart()
    apple_pencil_product = Product(name="Apple Pencil")
    sonny_product = Product(name="Sony Wireless headphone")
    cart.add(apple_pencil_product)
    cart.add(sonny_product)
    cart.add(apple_pencil_product)
    cart.delete(apple_pencil_product)
    return {"products": cart.products.__str__(), "deleted_products": cart.deleted_products}