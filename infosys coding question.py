# def calculateNumberOfBuses(N,Q,U,V,X,Y):
#     num = n
#     # If given number is greater than 1
#     if num > 1:
#     	# Iterate from 2 to n / 2
#     	for i in range(2, int(num/2)+1):
#     		# If num is divisible by any number between
#     		# 2 and n / 2, it is not prime
#     		if (num % i) == 0:
#     			print(num, "is not a prime number")
#     			break
#     	else:
#     		print(num, "is a prime number")
#     else:
#     	print(num, "is not a prime number")

#     return 2*N

def calculateNumberOfBuses(N,Q,U,V,X,Y):
    prime = 2
    if((N-1)==prime):
        return 2
    else:
        allList = U + V + X + Y
        allListSet = set(allList)
        if(len(allListSet)%2==0):
            return len(allListSet)
        else:
            return 2*N
    
n = int(input())
m = int(input())
q = int(input())
u,v,x,y = [],[],[],[]
for i in range(m):
    u.append(int(input()))
for i in range(m):
    v.append(int(input()))
for i in range(q):
    x.append(int(input()))
for i in range(q):
    y.append(int(input()))


print(calculateNumberOfBuses(n,q,u,v,x,y))
# print(u,v,x,y)
# l = u + v + x + y
# lis = set(l)
# print(lis)
# if(len(lis)!=n):
#     print(len(lis)*2)
# else:
#     print(2)
# u,v,x,y = set(u),set(v),set(x),set(y)
# print(u,v,x,y)
# length_u,length_v,length_x,length_y,flag_u,flag_v,flag_x,flag_y = 0,0,0,0,0,0,0,0
# if(len(u)==2):
#     length_u = 1
#     flag_u = 1
# if(len(v)==2):
#     length_v = 1
#     flag_v=1
# if(len(x)==2):
#     length_x = 1
#     flag_x = 1
# if(len(y)==2):
#     length_y = 1
#     flag_y = 1
# if(flag_y==1):
#     print(len)
# # print(calculateNumberOfBuses(n,q,u,v,x,y))
# def most_frequent(List):
#     return max(set(List), key = List.count)
# print(most_frequent(l)*n)


