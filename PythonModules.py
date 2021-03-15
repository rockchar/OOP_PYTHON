''' 
here we will see some python module classes 
'''

from collections import Counter

#lets create a list 

my_list = [11,2,2,2,2,23,3,3,3,3,3,4,4,4,4,11,23,9,9,9,9,9]
print(Counter(my_list))

sentence = "how many times each word will appear in this sentence. the words can be counted using the counter as they appear"
#print(sentence.split())

print(Counter(sentence.split()))

c= Counter(sentence)
print(c.most_common())

print(list(c))  #prints the unique elements in the sentnce 


from collections import defaultdict
my_def_dict = defaultdict(lambda:0)

my_def_dict["Correct"] = 1000
print(my_def_dict["Correct"])
print(my_def_dict["Wrong"])





from collections import namedtuple


Dog = namedtuple("Dog",["name","age","breed"])

sammy = Dog(name="Sammy",age=10,breed="Huskey")

print(sammy.name)
print(sammy.age)
print(sammy.breed)

list_e = [1,2,3,4,5,6]
print(list(list_e))
print(list(map(lambda x: x**x,list_e)))