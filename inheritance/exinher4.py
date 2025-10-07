class vehicle():
    def category(self):
        print("transport")
class car(vehicle):
    def cwheels(self):
        print("4 wheeler")
class bike(car):
    def bwheels(self):
        print("2 wheeler")

a=bike()
a.cwheels()
a.bwheels()

