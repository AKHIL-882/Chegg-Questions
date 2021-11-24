# recursive function
def nCr(n, r):
    return (fact(n) / (fact(r) * fact(n - r)))
# finding the factorial
def fact(n):
    res = 1
    for i in range(2, n+1):
        res = res * i
    return res
# getting values from user
n = int(input())
r = int(input())
# displaying the result
print(int(nCr(n, r)))