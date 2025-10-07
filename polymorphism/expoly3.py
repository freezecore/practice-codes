class vehicle():
    
    def start(self):
        print("starting vehicle")
class car(vehicle):
    
    def start(self):
        print("starting car by keyless ignition")
        
a=car()
a.start()

b=vehicle()
b.start()
