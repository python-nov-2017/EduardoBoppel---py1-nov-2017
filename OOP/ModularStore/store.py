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
            product.display_info()



if __name__ == "__main__":
    store1 = Store("Family Warehouse", "15 Main St", "Elmo")
    store2 = Store("Corner Bakery", "428 East Rd", "Cookie Monster")
    store3 = Store("CoffeeRoast", "115 River Ave", "John Barista")
    
    store1.inventory()
    store2.inventory()
    store3.inventory()
