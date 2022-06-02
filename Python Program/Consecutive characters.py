
# defing the function consecutive with list of strings
def consecutive(listofStrings):
    # variable to concatenate the list of strings
    testStr = ''
    # concatenating the listofStrings
    for i in listofStrings:
        test_str+=i
    # defining the size
    size = 3
    # iterating over the string
    for i, ele in enumerate(testStr):
        # calculating the sub string 
        substr = ele * size
        # checking the condition satisfies or not
        if test_str[i : i + size] == substr:
            # return true
            return True
        else:
            # return flase
            return False
# getting list of strings from user
listofStrings = [str(n) for n in input().split()]
# calling the function and displaying the result
print(consecutive(listofStrings))