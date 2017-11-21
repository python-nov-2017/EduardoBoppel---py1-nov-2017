from store import Store
from product import Product

myStore = Store("Corner Bakery", "15 Main Street", "Mrs Fields")

myStore.add_product(Product(15, "Hammer", "15kg", "Brand A"))
myStore.add_product(Product(12, "Nail", "5kg", "Brand B"))
myStore.add_product(Product(17, "Saw", "10kg", "Brand C"))
myStore.inventory()

myStore.products[0].add_tax(0.05).sell()
myStore.products[1].add_tax(0.05).sell().return_item("opened")
myStore.products[2].add_tax(0.05).sell().return_item('defective')
myStore.inventory()

myStore.remove_product("Saw")
myStore.inventory()