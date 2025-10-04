class calculator():
    def __init__(self,a,b):
        self.num1=a
        self.num2=b
    def display(self):
        print("sum:",self.num1+self.num2)
a=calculator(10,30)
a.display()
