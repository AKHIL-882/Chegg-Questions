# getting input from user
password = input()
# setting the flag bit to false
flag = False
# checking condition of length 8 
if(len(password)==8):
    # iterating over the input
    for i in password:
        # checking the value is a character
        if(i.isalpha()):
            flag = True
        # checking the value is a digit
        elif(i.isdigit()):
            flag = True
        else:
            flag=False # for another characters
            break
# displaying the result
if(flag==True):
    print("Valid Password")
else:
    print("Not a valid Password")