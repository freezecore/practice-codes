class employee:
    def details(self,a,b):
        self._name=a
        self._salary=b
    def display(self):
        print(self._name)
        print(self._salary)
        
a=employee()
a.details("asha",50000)
print(a._name)
print(a._salary)
