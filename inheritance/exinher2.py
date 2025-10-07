class father():
    def fskill(self):
        print("carpentry")
class mother():
    def mskill(self):
        print("paiting")
class child(father,mother):
    def name(self):
        print("alex")

a=child()
a.name()
a.fskill()
a.mskill()

