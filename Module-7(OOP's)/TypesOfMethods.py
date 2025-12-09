class Add:
    age=20
    @classmethod
    def displayAge(cls):
        print(cls.age)
        
    def __init__(self,name):
        self.name=name
    @staticmethod
    def add(a,b):
        return a+b
    def display(self):
        print(self.name)
a=Add('abc')
print(Add.add(2,3))
a.display()
Add.displayAge()