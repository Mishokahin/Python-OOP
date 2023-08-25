from typing import List

from project.product import Product


class ProductRepository:
    def __init__(self) -> None:
        self.products: List[Product] = []

    def add(self, product: Product) -> None:
        self.products.append(product)

    def find(self, name: str) -> Product:
        product = [p for p in self.products if p.name == name]
        if product:
            return product[0]

    def remove(self, product_name: str):
        product_to_remove = self.find(product_name)
        if product_to_remove in self.products:
            self.products.remove(product_to_remove)

    def __repr__(self) -> str:
        result = ""
        for p in self.products:
            result += f"{p.name}: {p.quantity}\n"
        return result[:-1]
