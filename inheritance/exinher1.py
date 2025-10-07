class animal():
    def speak(self):
        print("animal speaks")
class dog(animal):
    def bark(self):
        print("dog barks")

a=dog()
a.speak()
a.bark()

