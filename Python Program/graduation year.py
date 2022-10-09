# while loop
while 1:
    # getting the graduation year
    graduationYear = int(input("Enter the graduation year: "))
    # checking the condition
    if(graduationYear>1920 and graduationYear<2010):
        # displaying the resultzs
        print("The graudation year is in between 1920 and 2010")
        break
    else:
        # contining again
        print("Try again! :")
        continue