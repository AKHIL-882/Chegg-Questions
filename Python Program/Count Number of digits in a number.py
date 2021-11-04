# defining the function
def num_digit(n):
    count=0
    # while loop to iterate over the values
    while(n>0):
        # counting the digits
        count=count+1
        n=n//10
    # returing the count
    return count

# displaying the result and function calling
print(num_digit(123))
print(num_digit(1234))
print(num_digit(67812))