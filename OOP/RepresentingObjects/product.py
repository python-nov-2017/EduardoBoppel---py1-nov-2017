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
        return self.price

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
        print "Price: ", self.price
        print "Name: ", self.name
        print "Weight: ", self.weight
        print "Brand: ", self.brand
        print "Status: ", self.status
        return self


    def __repr__(self):
        return "<Product object, name: {}, price: {}, brand: {}, weight: {}, status: {} >".format(self.name, self.price, self.brand, self.weight, self.status)


if __name__ == "__main__":
    product1 = Product(15, "Hammer", "15kg", "Brand A")
    product2 = Product(12, "Nail", "5kg", "Brand B")
    product3 = Product(17, "Saw", "10kg", "Brand C")


    product1.display_info()
    product1.add_tax(0.12)
    product1.sell().display_info()
    product1.return_item("opened").display_info()

    product2.display_info()
    product3.display_info()


