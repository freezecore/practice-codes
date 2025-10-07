class circle():
    
    def perimeter(self,a,b):
        self.length=a
        self.breadth=b
    def area(self):
        print("area:",self.length*self.breadth)

class rectangle():
    
   def perimeter(self,a,b):
        self.length=a
        self.breadth=b
   def area(self):
        print("area:",self.length*self.breadth)
a=circle()
a.perimeter(10,20)
a.area()

b=rectangle()
b.perimeter(10,30)
b.area()
