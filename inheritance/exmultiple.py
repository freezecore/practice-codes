class human():
    def tech(self):
        print("phone")
class animal(human):
    def eat(self):
        print("animal eats")
class mammal(animal):
    def walk(self):
        print("mammal walks")
class dog(mammal):
    def bark(self):
        print("dog barks")

a=dog()
a.tech()
a.bark()
a.walk()
a.eat()
