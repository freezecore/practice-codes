class rectangle():
    def __init__(self,a,b):
        self.length=a
        self.width=b
    def area(self):
        print("area of rectangle:",self.length*self.width)
a=rectangle(2,25)
a.area()
