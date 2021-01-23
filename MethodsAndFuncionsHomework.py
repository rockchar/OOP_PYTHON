''' Q1 : Write a function that computes the volume of a sphere given its radius.

    The volume of a sphere is given as 43π𝑟3   
'''
import math
import string
from string import ascii_lowercase

def SphereVol(radius):
    #radius = input("Enter the radius:")
    volume = (4*math.pi*(int(radius)**3))/3
    return volume


print(SphereVol(2))


''' Q2 : Write a function that checks whether a number is in a given range (inclusive of high and low)
    def ran_check(num,low,high):
    pass
    # Check
    ran_check(5,2,7)
    5 is in the range between 2 and 7
    If you only wanted to return a boolean:
    def ran_bool(num,low,high):
    pass
    ran_bool(3,1,10)
    True    '''

def ran_check(num,low,high):
    if num in range(low,high,1):
        print("{} is in the range between {} and {}".format(num,low,high))

ran_check(5,2,7)


''' Q3 : Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.

    Sample String : 'Hello Mr. Rogers, how are you this fine Tuesday?'
    Expected Output : 
    No. of Upper case characters : 4
    No. of Lower case Characters : 33

    HINT: Two string methods that might prove useful: .isupper() and .islower()

    If you feel ambitious, explore the Collections module to solve this problem!

    def up_low(s):

    pass

    s = 'Hello Mr. Rogers, how are you this fine Tuesday?'

    up_low(s)

    Original String :  Hello Mr. Rogers, how are you this fine Tuesday?
    No. of Upper case characters :  4
    No. of Lower case Characters :  33

'''

string = 'Hello Mr. Rogers, how are you this fine Tuesday?'

def up_low(s):
    count_upper = 0
    count_lower = 0
    for element in s:
        if element.islower() and element.isalpha():
            count_lower += 1
        elif element.isalpha():
            count_upper += 1

    print("Original String : {}".format(s))
    print("No. of Upper case characters :  {}".format(count_upper))
    print("No. of Lower case Characters :  {}".format(count_lower))


    
    
up_low(string)

'''
Q4: Write a Python function that takes a list and returns a new list with unique elements of the first list.

Sample List : [1,1,1,1,2,2,3,3,3,3,4,5]
Unique List : [1, 2, 3, 4, 5]


'''

def unique_list(lst):
    un1lst = set(lst)
    print(un1lst)


lst =  [1,1,1,1,2,2,3,3,3,3,4,5]
unique_list(lst)

'''
Write a Python function to multiply all the numbers in a list.

Sample List : [1, 2, 3, -4]
Expected Output : -24
'''

def multiply_list(lst):
    product=0
    for num in lst:
        if product == 0:
            product = num
        else:
            product *= num
    print(product)

lst = [1, 2, 3, -4]
multiply_list(lst)
        
'''
Write a Python function that checks whether a word or phrase is palindrome or not.

Note: A palindrome is word, phrase, or sequence that reads the same backward as forward, 
e.g., madam,kayak,racecar, or a phrase "nurses run". Hint: You may want to check out the .replace() method in a string 
to help out with dealing with spaces. Also google search how to reverse a string in Python, 
there are some clever ways to do it with slicing notation.

'''

def palindrome(str):
    new_str = str.replace(" ","")
    length = len(new_str)
    s1 = slice(0,math.floor(length/2))
    #s2 = slice(math.ceil(length/2),length)
    #print(new_str[s1])
    str1 = new_str[s1]
    str2 = new_str[::-1][s1]
    if str1 == str2:
        print("palindrome")
    else:
        print("not palindrome")


str = "nurses run"
palindrome(str)

'''
Write a Python function to check whether a string is pangram or not. (Assume the string passed in does not have any punctuation)

Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
For example : "The quick brown fox jumps over the lazy dog"

Hint: You may want to use .replace() method to get rid of spaces.

Hint: Look at the string module

Hint: In case you want to use set comparisons

'''

def is_anagram(str1):
    test_str = str1.replace(" ","")
    list_str = list(set(test_str.lower()))
    ascii_lowercase = "abcdefghijklmnopqrstuvwxyz"
    sorted_string=""
    #print(list_str)
    #joined_string = joined_string.join(list_str)
    #print(test_str)
    sorted_string = sorted_string.join(sorted(list_str))
    print(sorted_string)
    if ascii_lowercase == sorted_string.lower():
        print("Pangram")
    else:
        print("not Pangram")
    
str = "Two driven jocks help fax my big quiz"
is_anagram(str)