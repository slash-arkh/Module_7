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
        self.__file_name = 'products.txt'

    def get_products(self):
        list_ = open(self.__file_name, 'r')
        product = list_.read()
        return product
        list_.close()

    def add(self, *products):
        for product in products:
            list_ = open(self.__file_name, 'a')
            current_products = self.get_products()
            if product.name in current_products:
                print(f'Продукт {product.name} уже есть в магазине')
                list_.close()
            else:
                list_.write(str(product) + '\n')
                list_.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__
s1.add(p1, p2, p3)
print(s1.get_products())



