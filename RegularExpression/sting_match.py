"""
Regular Expresssion (re)
Pattern Matching : 
Pattern    Exmaple          Description 
[A-Z]      UDOY             Match Only the Capital Latter 
[0-9]      123456           Match Only Numeric values 
[A-Za-z]   Udoy             Match Only Capital and Smaller value 
[Hmm**]    Hmm,Hmmm,Hmmm..  0 or more matching 
"""
import re 

#String Match
pattern = 'Udoy'

match = re.search(pattern,"My Name is aBC")

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



