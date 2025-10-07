class grandparent():
    def heritage(self):
        print("wisdom")
class parent(grandparent):
    def guidance(self):
        print("discipline")
class child(parent):
    def name(self):
        print("riya")

a=child()
a.name()
a.guidance()
a.heritage()

