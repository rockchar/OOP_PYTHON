class Animal():
    def __init__(self):
        print("animal Created")

    def eat(self):
        print("I am an animal eating")


class Dog(Animal):
    def __init__(self,name):
        Animal.__init__(self)
        self.name = name

    def speak(self):
        return self.name+" Says woof!"


class Cat(Animal):
    def __init__(self,name):
        Animal.__init__(self)
        self.name = name

    def speak(self):
        return self.name+" Says meaw!"


rocky = Dog("rocky")
print(rocky.speak())

felix = Cat("felix")
print(felix.speak())


rocky.eat()

#lets see an example

for pet in [rocky,felix]:
    print(pet.speak())