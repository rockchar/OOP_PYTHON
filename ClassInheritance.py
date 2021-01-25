''' here we will discuss class inheritance '''

class Animal():
    def __init__(self,type,name):
        print("animal created")
        self.type=type
        self.name=name
    def who_am_i(self):
        print("I am an animal")

    def eat(self):
        print("I am an animal eating")


class Dog(Animal):
    def __init__(self):
        Animal.__init__(self,type="Domestic",name="dog")
        print("Dog Created")
    #overriding the class method
    def eat(self):
        print("I am a Dog eating food")
    def bark(self):
        print("woof")


dog = Dog()
print(dog.name)
print(dog.type)
dog.eat()
dog.bark()
dog.who_am_i()