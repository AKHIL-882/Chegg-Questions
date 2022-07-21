N = int(input())
X = int(input())
arr = [int(n) for n in input().split()]
arr_new = arr * X
arr_new.sort()
Q = int(input())
pos= [int(n) for n in input().split()]
new_arr = []
for i in pos:
    new_arr.append(arr_new[i])
print(new_arr)