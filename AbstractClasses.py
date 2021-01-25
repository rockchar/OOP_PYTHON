''' 
    This will demonstrate an abstract class 
    An abstract class is a class which we do not expect to be instantiated
'''

class Animal():
    def __init__(self,name):
        self.name = name
    
    def speak(self):
        raise NotImplementedError("Derived class/subclass must implement this method")


animal = Animal("cow")
animal.speak()