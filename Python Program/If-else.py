# defining the function 
def shampoo_instructions(num_cycles):
    # condition to check num_cycles are less then 1
    if num_cycles<1:
        print("Too few")
    # condition to check num_cycles are greather then 4
    elif(num_cycles>4):
        print("Too many")
    # else print Lather and rinse
    else:
        print(str(num_cycles) +": " + "Lather and rinse")
# getting the input from the user
num_cycles = int(input())
# iterating over the loop
for i in range(1,num_cycles+1):
    #calling the function
    shampoo_instructions(i)