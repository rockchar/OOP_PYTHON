#here we will discuss the regular expresssions in python
#import the regular expression module
import re
pattern = "phone"

text = "the agents phone number is 400-500-600"

print(pattern in text)

#now lets search the pattern using regular expressions
print(re.search(pattern,text))

#lets assign a match object 
match = re.search(pattern,text)

#now we can use the inbuilt functions in the match object like span,start(start of index),end(end of index)
print(match.span())
print(match.start())
print(match.end())

#NOTE: Match ends at the first match. For multiple matches we need
#match all

#now lets check multiple matches
text = "My phone once and my phone twice "
matches = re.findall(pattern,text)
print(matches)
print(len(matches))
#we can also get the iterator for getting more detailed information
#so for that we have a for loop
for match in re.finditer(pattern,text):
    print(match)
    print(match.span())
    print(match.group())#actual text of the pattern


#************************************** Regular expressions for general patterns **************************************

'''
Problem statement : a phone number is of the format 555-555-5555
                    Lets write a regular expression to parse phone numbers in a text

'''

text = "Phone number home is 111-222-3344 and office is 222-333-4455"
#now we create a regular expression for the same thing
pattern=r"\d\d\d-\d\d\d-\d\d\d\d"
matches=re.findall(pattern,text)
print(len(matches))

for match in re.finditer(pattern,text):
    print (match.group())
    print (match.span())