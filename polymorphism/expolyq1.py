class animal():
    def sound(self):
        print("some sound")
class dog(animal):
    def sound(self):
        print("bark")
        
class cat(animal):
    def sound(self):
        print("meow")

def make_it_sound(animal):
    print(animal.sound())

a=dog()
b=cat()
c=animal()

make_it_sound(a)
make_it_sound(b)
make_it_sound(c)

'''


class Animal:
    def sound(self):
        return "Some sound"
class Dog(Animal):
    def sound(self):
        return "Bark"
class Cat(Animal):
    def sound(self):
        return "Meow"

def make_it_sound(animal):
    print(animal.sound())

a = Animal()
d = Dog()
c = Cat()

make_it_sound(a)  # Output: Some sound
make_it_sound(d)  # Output: Bark
make_it_sound(c)  # Output: Meow   
'''
