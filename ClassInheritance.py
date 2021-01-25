''' here we will discuss class inheritance '''

class Animal():
    def __init__(self,type,name):
        print("animal created")
        self.type=type
        self.name=name


class Dog(Animal):
    def __init__(self):
        Animal.__init__(self,type="Demestic",name="dog")
        print("Dog Created")


dog = Dog()
print(dog.name)