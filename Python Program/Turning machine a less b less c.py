# importing the counter module
from collections import Counter
# getting the input string from user
my_str = input()
counter = Counter(my_str)
# counting the occurrance of variables
acount = counter['a']
bcount = counter['b']
ccount = counter['c']
# condition checking and display result
if(acount<bcount<ccount):
    print("Language Accepted\n")
else:
    print("Language not Accepted\n")
    
