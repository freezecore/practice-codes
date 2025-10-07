class employee:
    def details(self):
        self.name="asha"
        self._salary=50000
    def display(self):
        print(self.name)
        print(self._salary)
        
a=employee()
a.display()
