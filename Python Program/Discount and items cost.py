# creating a function with the parameters
def fun_function(n_items,cost_per_item,discount_percentage,discount_threshold):
    cost = n_items * cost_per_item
    if n_items>discount_threshold:
        cost = cost * (1-discount_percentage/100)
    return cost
# calling the main function
if __name__=="__main__":
    # function calling
	cost = fun_function(5,31,15,10)
	# display result
	print('5 items purchased at a cost of ${:.2f}'.format(cost))