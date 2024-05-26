class Product:
    def __init__(self, _name, _price):
        self.name = _name
        self.price = _price
        print("product nesnesi üretildi")

p1 = Product("Samsung s24 Ultra", 70000)
p2 = Product("Iphone 15 Pro MAX", 100000)

print(p1.name, p1.price)
print(p2.name, p2.price)