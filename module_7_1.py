from pprint import pprint
class Product:
    def __init__(self, name: str, weight: float, category: str):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'

class Shop(Product):
    def __init__(self):
        self.__file_name = 'product.txt'

    def get_products(self):
        file = open(self.__file_name, 'r')
        products = file.read().strip()
        file.close()
        return products

    def add(self, *products):
        existing_products = self.get_products()
        for product in products:
            if product.name in [p.split(', ')[0] for p in existing_products]:
                print(f'Продукт {product.name} уже есть в магазине')
            else:
                file = open(self.__file_name, 'a')
                file.write(str(product) + '\n')
                file.close()