# defining the function
def plus_one(x):
    # returing the result by adding 1 to each element
    y = [i+1 for i in x]
    return y
# getting values from user
x = [int(i) for i in input().split()]
# displaying the result
print(plus_one(x))