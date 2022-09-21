# function declaration
def subarraySum(arr, n):
    # declarating temperory variables
	temp,result = 0,0
    # lopping over the values 
	for i in range(0, n):
		temp=0;
		for j in range(i, n):
		    # calculating the start and end 
		    # point of values
			temp+=arr[j]
			result += temp
	# returing the result
	return result

# user input list
arr = [int(i) for i in input().split()]
# function calling and displaying the result
print(subarraySum(arr, len(arr)))
