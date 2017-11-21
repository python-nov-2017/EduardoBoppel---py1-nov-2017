class Store(object):
    def __init__(self, name, location, owner):
        self.name = name
        self.location = location
        self.owner = owner
        self.products = []
        

    def add_product(self, product):
        self.products.append(product)
        print "Added Product: ", product.name

    def remove_product(self, product):    
        for prod in self.products:    
            if prod.name == product:
                print "Removed product: ", prod.name
                self.products.remove(prod)
                return
                
        print "Product does not exist"
        

    def inventory(self):
        print "\n Store Inventory:"

        for product in self.products:
            print product.display_info()


    def __repr__(self):
        return "<Store object, name: {}, location: {}, owner: {}, products: {} >".format(self.name, self.location, self.owner, self.products)




if __name__ == "__main__":
    store1 = Store("Family Warehouse", "15 Main St", "Elmo")
    store2 = Store("Corner Bakery", "428 East Rd", "Cookie Monster")
    store2 = Store("CoffeeRoast", "115 River Ave", "John Barista")


    store1.add_product(Product(15, "Hammer", "15kg", "Brand A"))
    store1.add_product(Product(12, "Nail", "5kg", "Brand B"))
    store1.inventory()

    store1.add_product(Product(17, "Saw", "10kg", "Brand C"))
    store1.inventory()

    store1.remove_product("Nail")
    store1.inventory()
    
    #product1.display_info()
    #product1.add_tax(0.12)
    #product1.sell().display_info()
    #product1.return_item("opened").display_info()

    #product2.display_info()
    #product3.display_info()


