class animal:

    def __init__(self,name,age):
        self.name=name
        self.age=age
    def intro(self):
        print("I'm a wildanimal")
    def details(self):
        print("my name is",self.name)
        print("my age is",self.age)
ob=animal("tiger", 13)
print(ob.intro())
print(ob.details())
