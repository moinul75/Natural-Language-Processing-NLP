"""
Regular Expresssion (re)
Pattern Matching : 
Pattern    Exmaple          Description 
[A-Z]      UDOY             Match Only the Capital Latter 
[0-9]      123456           Match Only Numeric values 
[A-Za-z]   Udoy             Match Only Capital and Smaller value not the numeric vlues 
[Hmm**]    Hmm,Hmmm,Hmmm..  0 or more matching 
Kleene and Clousure 
'+' : 1 or more 
'*' : 0 or more 
Example: new(s)* result is : new, news, newss, newssssss, news....
Example: news(s)+: result is : news, newsss, newss... 
"""
import re 

#String Match
pattern = 'Udoy'

match =re.match(pattern,"My Name is aBC")

if match: 
    print("Result is Matched")
else: 
    print("Result is not Matched")


#Dot(.) matching 
pattern = "ud.y"

match = re.match(pattern,'udoy')

if match: 
    print(f"result is matched and the result is {match} ")
else: 
    print('Not matched')

# numeric matched [0-9] 

pattern = "[0-9]"

matching = re.match(pattern,"123456789")

if matching: 
    print(f'Result is Mathced and the result is {matching}')

else: 
    print('Result is not matching')



#now kleene and Clousure 

wrd = 'new(s)*'
result = re.match(wrd,'news')

if result: 
    print(f'Pattern Matched {result}')
else: 
    print('Not matched')

nwrd = 'new(s)+'

result = re.match(nwrd,"new")

if result: 
    print(f'Pattern Matched {result}')
else: 
    print('Not matched')


# * and + in the middle (lo(v)+e)

ptrn = 'lo(v)+e'

result = re.match(ptrn,'lovve')

if result: 
    print(f'Pattern Matched {result}')

else: 
    print(f'not Matched')


#pipe sysmbol (|) work like Or logical Operator N.B: if a|b , and the pattern is ab , it not matched if and only there is either a or b (a/b) not ab 
ptrn = 's(u|i|n)m'

result = re.match(ptrn,"sum")

if result: 
    print(f'Pattern matched {result}')

else: 
    print('Pattern Not matched')







