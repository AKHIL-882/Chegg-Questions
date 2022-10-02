# function declaration
def Lab7A(n):
    # printing the rows
    for i in range(n):
        # printing the columns
        for i in range(n):
            # printing the stars
            print('*', end = '')
        print()
# getting input from user   
n = int(input("Please ebter a value for the size: "))
# displaying the statement
print("This is the requested {0}x{0} box: ".format(n))
# function calling
Lab7A(n)


    