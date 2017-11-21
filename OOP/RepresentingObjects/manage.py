from animal import *
from bike import Bike
from callcenter import *
from car import Car
from hospital import Patient, Hospital
from mathdojo import *
from product import *
from store import *

#ANIMAL OBJECT
turtle = Animal("DONATELLO")
print turtle

#DOG OBJECT
fido = Dog("FIDO")
print fido

#DRAGON OBJECT
puff = Dragon("PUFF")
print puff

#BIKE OBJECT
bike1 = Bike(175, "18mph")
print bike1

#CALLCENTER OBJECT
myCallCenter = CallCenter()
print myCallCenter

#CALL OBJECT
myCall = Call(1, "John", "123-123-1234", "1:06", "Inquiry")
print myCall

#CAR OBJECT
myCar = Car(2000, "35mph", "Full", "15mpg")
print myCar

#HOSPITAL OBJECT
myHospital = Hospital("General Hospital", 3)
print myHospital

#PATIENT OBJECT
myPatient = Patient("George", "Nuts" )
print myPatient

#MATHDOJO OBJECT
md = MathDojo()
print md

#STORE OBJECT
myStore = Store("CoffeeRoast", "115 River Ave", "John Barista")
print myStore

#PRODUCT OBJECT
myProduct = Product(15, "Hammer", "15kg", "Brand A")
print myProduct

