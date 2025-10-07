class bankaccount:
    def details(self,a):
        self.__balance=a
    def display(self):
        print(self.__balance)
        
a=bankaccount()
a.details(1000)
a.display()
