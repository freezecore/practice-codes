class livewire():
    name=''
    age=''
    dept=''
    def display(self):
        print("name:",self.name)
        print("age:",self.age)
        print("department:",self.dept)

aname=livewire()

aname.name="livewire"
aname.age="30"
aname.dept="IT"

aname.display()
