class Book():
    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages

   #string representation
    def __str__(self):
        return f"{self.title} by {self.author}"

    #length representation(no of pages)
    def __len__(self):
        return self.pages


book = Book("Treasure Island","Robert Lewis Stevension",532)
print(book)

print(len(book))

''' the following is an example class containing all the special methods 
    What Are Dunder Methods?
    In Python, special methods are a set of predefined methods you can use 
    to enrich your classes. They are easy to recognize because they start 
    and end with double underscores, for example __init__ or __str__.
    Dunder methods let you emulate the behavior of built-in types. 
    For example, to get the length of a string you can call len('string'). 
    But an empty class definition doesn’t support this behavior out of the 
    box.
    https://dbader.org/blog/python-dunder-methods
'''
class Account():
    """ A Simple Account Class """
    def __init__(self,name,accountbalance=0):
        """ Object Initialization __init__
        This is the constructor that allows us to create the objects
        of this class default amount is 0 """
        self.name = name
        self.accountbalance = accountbalance
        self.transcactions   = []

    def __repr__(self):
        """ The “official” string representation of an object. 
        This is how you would make an object of the class. 
        The goal of __repr__ is to be unambiguous."""
        return f"Account({self.name},{self.accountbalance})"

    def __str__(self):
        """The “informal” or nicely printable string representation of an 
        object. This is for the enduser."""
        return "Account of {} starting with balance {}".format(self.name,self.accountbalance)


    def addtransaction(self,amount):
        if not isinstance(amount,int):
            raise ValueError("please use integer for amount")
        else:
            self.transcactions.append(amount)




ac = Account("rohit",500)
print(repr(ac))
print(ac)
