# funtion to get the key in dictionary 
def get_key(val):
    # iterating over the dictionary 
    for key, value in synonyms.items():
        # condition checking
        if val == value:
            # returning the key
            return key
    # if key doesn't found
    return "key doesn't found"
# dictionary  to store inputs
synonyms = {}
# getting the size of dictionary 
n = int(input())
# iterating over the size
for i in range(n):
    # getting inputs from user
    userValues = [n for n in input().split()]
    # adding to the dictionary 
    synonyms[userValues[0]] = userValues[1]
# getting the value from user
userRequest = input()
# function calling and displaying the result
print(get_key(userRequest))
