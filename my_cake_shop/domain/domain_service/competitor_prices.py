from my_cake_shop.domain.models import Price, Product

COMPETITOR_PRICES = {"Apple Pencil": Price(amount=1), "Sony Wireless headphone": Price(amount=1)}


class CompetitorPrices:
    competitor_prices: dict = COMPETITOR_PRICES

    def calculate_discounted_price(self, product: Product):
        return self.competitor_prices[product.name].discounted_by(0.1)
