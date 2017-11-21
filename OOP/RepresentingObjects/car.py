class Car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if price > 10000:
            self.tax = 0.15
        else:
            self.tax = 0.12

    def display_all(self):
        print "Price: ", self.price
        print "Speed: ", self.speed
        print "Fuel: ", self.fuel
        print "Mileage: ", self.mileage
        print "Tax Rate: ", self.tax

    def __repr__(self):
        return "<Car object price: {}, speed: {}, fuel: {}, mileage: {}>".format(self.price, self.speed, self.fuel, self.mileage)


if __name__ == "__main__":
    car1 = Car(2000, "35mph", "Full", "15mpg")
    car2 = Car(1500, "5mph", "Not Full", "105mpg")
    car3 = Car(2500, "45mph", "Full", "20mpg")
    car4 = Car(4000, "50mph", "Not Full", "15mpg")
    car5 = Car(5000, "50mph", "Full", "0mpg")
    car6 = Car(1700, "28mph", "Full", "30mpg")