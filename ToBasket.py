class Basket:
    def __init__(self, max_weight):
        self.max_weight = max_weight
        self.product = []
        self.product_weight = []

    def add_to_container(self, value):
        self.product.append(prod.name)
        self.product_weight.append(prod.weight)
        print('products in the {}: '.format(type(self).__name__), self.product)


    def container_selection(self, container):
        print('Куда положить (Basket/Package?)')
        container = input()
        if container == 'Basket':
            basket1.add_to_container(self)
        elif container == 'Package':
            package1.add_to_container(self)
        else:
            print('невозможно положить, нет такой тары')


class Package(Basket):
    pass
    # def add_to_package(self, value):
    #     self.product.append(prod.name)
    #     self.product_weight.append(prod.weight)
    #     print('products in the {}: '.format(type(self).__name__), package1.product)

class Products:
    print('Введите наименование продукта и вес: ')
    def set(self, name, weight_products):
        self.name = name
        self.weight = weight_products

basket1 = Basket(10)
package1 = Package(15)
prod = Products()

product = prod.set(input(), input())
basket1.container_selection(prod)
product = prod.set(input(), input())
basket1.container_selection(prod)
product = prod.set(input(), input())
basket1.container_selection(prod)
print('products in the {}: '.format('Basket'), basket1.product)
print('products in the {}: '.format('Package'), package1.product)
print('weight in basket', basket1.product_weight)
print('weight in package', package1.product_weight)
