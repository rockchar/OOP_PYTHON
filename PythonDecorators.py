'''

'''

#let us define a simple function

def fun():
    return 1

def sayhello():
    return "Hello!!"

greet = sayhello

print(greet())

print(sayhello)
print(greet)


# sayhello object is deleted but another function object 
# greet is still referring to it
# functions are objects that can be passed to another objects


print(greet()) #still points to 

'''
lets see another example. We will write a simple function
'''

def hello(somefun):
    print("the hello() function has been executed")

    #lets define a function within this function
    def greet():
        return '\t The greet() function inside the hello() function!'
    #lets define another function welcome
    def welcome():
        return '\t The welcome() function inside the hello() function'

    print(greet())
    print(welcome())
    print("This is the end of hello()")




def func_to_decorate(originalfn):
    print("Before the function call")
    originalfn()
    print("after the function call")



@func_to_decorate
def fun_need_decoration():
    print('this function needs decoration')



