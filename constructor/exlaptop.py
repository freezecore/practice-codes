class laptop():
    charger_type="c-type"
    def __init__(self,a,b,c,d):
        self.ram=a
        self.rom=b
        self.processor=c
        self.price=d
    
    def lap1(self):
        print(self.ram)
        print(self.rom)
        print(self.processor)
        print(self.price)
        print(self.charger_type)
        
d=laptop("64gb","256gb","intel","25k")
d.lap1()
print()

s=laptop("32gb","128gb","snapdragon","30k")
s.lap1()
print()
g=laptop("20gb","18gb","snap","3k")
g.lap1()
