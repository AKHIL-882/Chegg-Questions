# provided list
LIST = [5,26,33,"5",115,120,9,"0",88,1]
# iterating over the list
for i in LIST:
    # checking the values is an instance of
    # integer
    if(isinstance(i, (int))):
        # condition for even 
        if(i%2==0):
            print(str(i) + " is even")
        else: 
            print(str(i) + " is odd") #displaying the odd
    else:  
        print("\'" + i + "\'" + " is a string") # displaying the string


