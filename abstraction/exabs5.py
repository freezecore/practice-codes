from abc import ABC,abstractmethod
class vehicle(ABC):
    @abstractmethod
    def accelerate(self):
        pass
    @abstractmethod
    def park(self):
        pass

class bike(vehicle):
    def accelerate(self):
        print("bike is accelerating @60km/hr")
    def park(self):
        print("bike is parked at two-wheeler parking")
class car(vehicle):
    def accelerate(self):
        print("car is accelerating @90km/hr")
    def park(self):
        print("car is parked at four-wheeler parking")

a=bike()
b=car()
b.accelerate()
b.park()
a.accelerate()
a.park()
