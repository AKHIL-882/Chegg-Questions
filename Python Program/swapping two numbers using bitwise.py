x = int(input())
y = int(input())
 
# Swapping using bitwise xor
x = x ^ y
y = x ^ y
x = x ^ y

print("Value of x:", x)
print("Value of y:", y)