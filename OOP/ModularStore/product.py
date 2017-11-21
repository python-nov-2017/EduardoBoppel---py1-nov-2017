class Product(object):
    def __init__(self, price, name, weight, brand):
        self.price = price
        self.name = name
        self.weight = weight
        self.brand = brand
        self.status = "For Sale"

    def sell(self):
        self.status = "Sold"
        return self

    def add_tax(self, tax):
        self.price *= (1+tax)
        return self

    def return_item(self, reason):
        if reason == "defective":
            self.status = "defective"
            self.price = 0
        elif reason == "new":
            self.status = "For Sale"
        elif reason == "opened":
            self.status = "Used"
            self.price *= 0.80
        else:
            print "Select a valid return reason"
        return self

    def display_info(self):
        print "Name: {}, Price: {}, Brand: {}, Weight: {}, Status: {}".format(self.name, self.price, self.brand, self.weight, self.status)




if __name__ == "__main__":
    prod1 = Product(15, "Hammer", "15kg", "Brand A")
    prod2 = Product(12, "Nail", "5kg", "Brand B")
    prod3 = Product(17, "Saw", "10kg", "Brand C")

    prod1.display_info()
    prod2.display_info()
    prod3.display_info()

    prod1.add_tax(0.12)
    prod1.sell()
    prod1.return_item("defective")
    prod1.display_info()
    
    prod2.add_tax(0.12)
    prod2.sell()
    prod2.return_item("new")
    prod2.display_info()

    prod3.add_tax(0.12)
    prod3.sell()
    prod3.return_item("opened")
    prod3.display_info()
