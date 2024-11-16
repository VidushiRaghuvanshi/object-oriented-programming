class parrot:
    species="bird"

    def __init__(self,name,age):
        self.name=name
        self.age=age
pigeons=parrot("pigeons",13)
sparrow=parrot("sparrow",14)
print("pigeons is a",pigeons.species)
print("sparrow is also a",sparrow.species)
print(pigeons.name,"is",pigeons.age,"years old")
print(sparrow.name,"is",sparrow.age,"years old")