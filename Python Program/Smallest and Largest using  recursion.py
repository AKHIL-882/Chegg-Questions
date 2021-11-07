# function to get the Smallest value
def findMinRec(A, n):
    if (n == 1):
        return A[0]
    return min(A[n - 1], findMinRec(A, n - 1))
# function to get the largest value
def findMaxRec(A, n):
    if (n == 1):
        return A[0]
    return max(A[n - 1], findMaxRec(A, n - 1))
  
# getting values from user
A = [int(n) for n in input().split()]
# uncomment the below code to predefine the list
# predefining the list  
# A = [1, 4, 45, 6, -50, 10, 2]
n = len(A)
# displaying the result
print("Smallest element is: ",findMinRec(A, n))
print("Largest element is: ",findMaxRec(A,n))
