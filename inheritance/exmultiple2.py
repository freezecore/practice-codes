class vehicle():
    def __init__(self):
        print("this is vehicle")
class twowheel(vehicle):
    def tw(self):
        print("this is two-wheeler")
class fourwheel(twowheel):
    def fw(self):
        print("this is four-wheeler")
class car(fourwheel):
    def car(self):
        print("this is car")

a=car()
a.fw()
a.tw()
a.car()
