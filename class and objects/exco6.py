class book():
    def __init__(self,a,b):
        self.title=a
        self.author=b
    def display(self):
        print("title:",self.title)
        print("author:",self.author)
a=book("python basics","john smith")
a.display()
