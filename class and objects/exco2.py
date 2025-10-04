class car():
    def __init__(self,a,b):
        self.brand=a
        self.model=b
    def display(self):
        print("car brand:",self.brand)
        print("car model:",self.model)
a=car("toyota","fortuner")
a.display()
