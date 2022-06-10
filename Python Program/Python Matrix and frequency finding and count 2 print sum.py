# importing the libraries
import numpy
# getting the size of matrix
n = int(input())
# getting user input values into matrix
mat = [[int(input()) for x in range (n)] for y in range(n)]
# finding the frequency of all numbers
(unique, counts) = numpy.unique(mat, return_counts=True)
sum_ = 0
# finding the values whose frequencies are more or equal to 2
for i in range(len(counts)):
    if(counts[i]>=2):
        sum_ = sum_ + unique[i]
# displaying the result
print(sum_)
        
