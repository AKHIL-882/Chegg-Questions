# defining the function
def sum_list(vals):
    N = len(vals)
    # base case
    if len(vals)== 0:
        return 0
    else:
        return vals[0]+sum_list(vals[1:])

# getting values from user
vals =[int(n) for n in input().split()]

# calling the function
ans =sum_list(vals )
print (ans)

