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
    #this is a class object attribute which will be same
    #for every instance of the class 
    carmaker = "toyota"
    speed = 0
    def __init__(self,color,topspeed):
        self.color = color
        self.topspeed = topspeed

    #lets define a method to acclerate the car
    def acclerate(self,speedincrease):
        self.speed=self.speed+speedincrease

    def showspeed(self):
        print(self.speed)


new_car = NewCar(color="red",topspeed=500)
print(new_car.carmaker)

new_car.showspeed()
new_car.acclerate(100)
new_car.showspeed()
new_car.acclerate(100)
new_car.acclerate(100)
new_car.showspeed()