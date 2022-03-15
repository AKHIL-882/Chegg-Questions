# enter number of terms
numberOfValues = int(input("Input the n value: "))+1 
# initiating the first two terms
number1, number2 = 0, 1
count = 0
# checking the number is valid or not
if numberOfValues <= 0:
   print("Please enter a positive integer")
# if there is only one term, return number1
elif numberOfValues == 1:
   print(number1)
# displaying the Fibonacci series
else:
   while count < numberOfValues:
       print(number1,end=",")
       nth = number1 + number2
       # update values
       number1 = number2
       number2 = nth
       count += 1