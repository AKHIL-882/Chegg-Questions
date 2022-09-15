# # defining the function
# def is_prime(n):
#     # interating over the list 
#     for x in n:
#         flag = False
#         if x > 1:
#             # checking for factors
#             for i in range(2, x):
#                 if (x % i) == 0:
#                     # if factor is found, set flag to True
#                     flag = True
#                     # break out of loop
#                     break
#         if flag:
#             print(x, "is not a prime number")
#         else:
#             print(x, "is a prime number")
# # getting user input
# n = [int(i) for i in input().split()]
# # function calling
# is_prime(n)

# function definition
def gen_prime(n):
    print("Prime numbers:",end=' ')
    count=0
    # iterating 
    ''' change the range function if you wish the 
    values from 1'''
    for n in range(2,numr*numr):
        if(count==numr):
            break
        # condition checking
        for i in range(2,n):
            if(n%i==0):
                break
        else:
            # printing the result
            print(n,end=' ')  
            count=count+1
# getting user value
numr=int(input("Enter range:"))
# function calling
gen_prime(numr)

