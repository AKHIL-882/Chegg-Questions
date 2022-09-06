# getting user value
userInput = input()
# slicing the digits
tenthPlace,onesPlace = int(userInput[-2]),int(userInput[-1])
# displaying the result
print(tenthPlace - onesPlace)
