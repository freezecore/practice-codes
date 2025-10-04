class person():
    def __init__(self,a,b):
        self.name=a
        self.city=b
    def display(self):
        print("hello,I am ",self.name,"from",self.city)
a=person("ravi","chennai")
a.display()
