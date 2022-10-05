# function declaration
def print_10_pattern(size):
    # iterating over the rows
    for i in range(n):
        for j in range(n):
            # displaying the result
            print((i+j+1)%2,end="")
        print()
    
# getting input from user
n = int(input())
# function calling
print_10_pattern(n)