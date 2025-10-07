class laptop():
    def lprice(self):
        print("laptop price")
class mobile():
    def pprice(self):
        print("mobile phones")
class computer(laptop,mobile):
    def cfiles(self):
        print("computer files")

a=computer()
a.lprice()
a.pprice()
a.cfiles()
