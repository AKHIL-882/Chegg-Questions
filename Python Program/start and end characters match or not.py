# defining the function
def sameStartEnd(myString):
    # checking the start and end characters are same or Not
    # here I am not considering the case sensitivity of characters
    # converting to lower case to check the start and end characters 
    # are matching or not.
    if(myString[0].lower()==myString[-1].lower()):
        return True
    else:
        return False
# displaying the result
print(sameStartEnd('MangoM'))
print(sameStartEnd('Mango'))
print(sameStartEnd('Manm'))