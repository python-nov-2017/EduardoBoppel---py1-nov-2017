class Bike(object):
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0

    def displayInfo(self):
        print self.price, self.max_speed, self.miles
        return self

    def ride(self):
        print "riding"
        self.miles += 10
        return self

    def reverse(self):
        if self.miles > 0:
            print "reversing"
            self.miles -= 5
        else:
            print "cannot reverse any more"
        return self

    def __repr__(self):
        return "<Bike object price: {}, max_speed: {}, miles: {}>".format(self.price, self.max_speed, self.miles)


if __name__ == "__main__":
    bike1 = Bike(175, "18mph")
    bike2 = Bike(200, "25mph")
    bike3 = Bike(250, "32mph")

    bike1.ride().ride().ride().displayInfo()
    bike2.ride().ride().reverse().reverse().displayInfo()
    bike3.reverse().reverse().reverse().displayInfo()