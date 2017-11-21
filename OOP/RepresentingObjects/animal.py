class Animal(object):
    def __init__(self, name):
        self.name = name
        self.health = 100

    def walk(self):
        self.health -= 1
        return self

    def run(self):
        self.health -= 5
        return self

    def display_health(self):
        print self.health

    def __repr__(self):
        return "<Animal object {}, health {}>".format(self.name, self.health)

class Dog(Animal):
    def __init__(self, name):
        super(Dog, self).__init__(name)
        self.health = 150

    def pet(self):
        print "Wagging Tail"
        self.health += 5
        return self

    def __repr__(self):
        return "<Dog object {}, health {}>".format(self.name, self.health)

class Dragon(Animal):
    def __init__(self, name):
        super(Dragon, self).__init__(name)
        self.health = 170

    def fly(self):
        print "I'm flying"
        self.health -= 10
        return self

    def display_health(self):
        super(Dragon, self).display_health()
        print "I am a Dragon"

    def __repr__(self):
        return "<Dragon object {}, health {}>".format(self.name, self.health)



if __name__ == "__main__":
    #ANIMAL OBJECT
    turtle = Animal("DONATELLO")
    print turtle.name
    turtle.display_health()
    turtle.walk().walk().walk().run().run()
    turtle.display_health()
    print turtle

    #DOG OBJECT
    fido = Dog("FIDO")
    print fido.name
    fido.display_health()
    fido.walk().walk().walk().run().run()
    fido.display_health()
    fido.pet()
    fido.display_health()
    print fido


    #DRAGON OBJECT
    puff = Dragon("PUFF")
    print puff.name
    puff.display_health()
    puff.fly()
    puff.display_health()
    #puff.pet()
    print puff
