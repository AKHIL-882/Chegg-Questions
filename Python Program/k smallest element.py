# function declaration
def kth_smallest(a_list, k):
    # sorting the list
    a_list.sort()
    # returing the value
    return a_list[k-1]
# uncomment the below list for different values
#p = [1,1,2,12,11,5,2,4,11,36,22,22,36,10,42,1,1,1,5,6]
#p = [2,1,2,12,11,5,2,4,11,34,22,22,34,10,62,1,1,1,5,6]
#p = [4,1,2,12,11,5,2,4,11,34,22,22,34,10,22,1,1,1,5,6]
p =  [3,2,12,11,5,2,3,11,10,22,12,12,5,6]
# getting value from user
k = int(input())
# removing duplications from list
p = [p[i] for i in range(len(p)) if i == p.index(p[i]) ]
# function calling and displaying the result.
print(kth_smallest(p,k))