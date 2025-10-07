class school():
    def motto(self):
        print("learn and grow")
class teacher(school):
    def role(self):
        print("teaching")
class student(school):
    def learn(self):
        print("learing")
class alumni(teacher):
    def status(self):
        print("graduated")

a=alumni()
a.motto()
a.role()
a.status()
