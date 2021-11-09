# defining the function
def findTriplet(a1, a2, a3,n1, n2, n3, sum):
    s = set()
    # iterating and adding the values
    for i in range(n1):
        s.add(a1[i])
    # forming the pairs
    for i in range(n2):
        for j in range(n3):
            if sum - a2[i] - a3[j] in s:
                return True
    return False
 
# initailizing the array
a1 = [1, -2, 3, 4, 5]
a2 = [2, 3, 6, -1, 2]
a3 = [3, 24, 5, 6]
# finding the length of the array
n1 = len(a1)
n2 = len(a2)
n3 = len(a3)
sum = 0
if findTriplet(a1, a2, a3,n1, n2, n3, sum) == True:
    print("True")
else:
    print("False")