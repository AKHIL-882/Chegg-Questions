# getting input from user
string = input("Enter text:").lower()
res = []
# iterating over the string
for i in string:
    # checking for the character is alphabet
    if((i >= 'a' and i <= 'z')):
        # finding the count of character
        frequency = string.count(i)
        # appending to the list
        res.append(str(i) + ":" + str(frequency))
# removing the duplicates
res = [*set(res)]
# iterating over the list 
sol = ""
for i in res:
    sol = sol + i + ","
# displaying the result
if(len(sol)<=0):
    print("your text does not contain any letter")
else:
    print("The count of letters in text is: [{0}]".format(sol.strip(',')))