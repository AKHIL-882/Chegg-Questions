# assigning the value
release_year = '1991'
# setting the boolean variable to False
correct = False
# iterating till the condition pass
while(1):
    # getting value from user
    answer = input("When was Python first released? ")
    # checking the user entered value is equal to 
    # initialized value
    if answer == release_year:
        # Congratulations message
        print('Congratulations! That is correct. ')
        # setting boolean variable to True
        correct = True
        break
    else:
        # re-try again
        print('No, that\'s not it. Try again\n')
        continue
print('Bye')