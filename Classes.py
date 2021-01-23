''' this file demostrates the basics of pythn classes '''

'''
lets create a basic class CAR and add attributes
'''

class Car():

    def __init__(self,color,topspeed):
        self.inscolor = color
        self.instopspeed = topspeed


my_car = Car(topspeed=100,color = "blue")
print(type(my_car))
print(my_car.instopspeed)
print(my_car.inscolor)

#Note by convention we need to use the same name for 
#the parameters and the atributes so we will have 
#another class for the same

class NewCar():

    def __init__(self,color,topspeed):
        self.color = color
        self.topspeed = topspeed

