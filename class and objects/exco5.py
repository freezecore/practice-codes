class circle():
    def __init__(self,r,pi):
        self.radius=r
        self.pi=pi
    def display(self):
        print("circumference:",(self.radius*self.pi*2))
a=circle(4,3.14)
a.display()
