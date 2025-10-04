class bankaccount():
    def __init__(self,a,b,c):
        self.accnum=a
        self.balance=b
        self.deposit=c
    def display(self):
        print("new balace:",self.balance+self.deposit)
a=bankaccount("",2000,300)
a.display()
