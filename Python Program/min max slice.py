# # input list
# list_variable = [100,144,169,1000,8]

# # use the below command if you want 
# # to get input from user
# #list_variable = [int(n) for i in input().split()]


# print("The largetst value in the list is: ",max(list_variable))
# print("The smallest value in the list is: ",min(list_variable))



# given prices
fare = "$10.00"
tip = "2.00$"
tax = "$ 0.80"
# slicing according to the values
fare = fare[1:]
tip = tip[:-1]
tax = tax[2:]
# type casting to float
total = float(fare)+float(tax)+float(tip)
# printing upto decimal places
format_float = "${:.2f}".format(total)
# displaying the result
print("The total trip cost is: ",format_float)

