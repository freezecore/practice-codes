class laptop():
    def __init__(self,a,b):
        self.brand=a
        self.price=b
    def display(self):
        print("laptop brand:",self.brand,",price:",self.price)
a=laptop("dell","55000")
a.display()
