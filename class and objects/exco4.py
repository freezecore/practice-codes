class employee():
    def __init__(self,a,b):
        self.name=a
        self.salary=b
    def display(self):
        print("employee:",self.name,",salary:",self.salary)
a=employee("kiran","45000")
a.display()
