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


REMEMBER THE FOLLOWING TABLE FOR REGULAR EXPRESSIONS

Character       Description     Example Pattern Code        Example Match
\d              A digit          file_\d\d                   file_25
\w              Alphanumeric     \w-\w\w\w                   a-123, b-12_3, b-1_23 etc.
\s              whitespace       \w\s\w\s\w                  a b c , 1 2 3 , _ _ _ etc
\D              A non digit      \D\D\D                      ABC, abc etc
\W              a non alphanum   \W\W\W\W\W                  **#>*,*()#&
\S              A non-whitespce  \S\S\S\S                    yoyo

'''

text = "Phone number home is 111-222-3344 and office is 222-333-4455"
#now we create a regular expression for the same thing
pattern=r"\d\d\d-\d\d\d-\d\d\d\d"
matches=re.findall(pattern,text)
print(len(matches))

for match in re.finditer(pattern,text):
    print (match.group())
    print (match.span())