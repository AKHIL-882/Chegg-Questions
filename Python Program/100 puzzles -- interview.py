n = [0 for i in range(100)]
for i in range(0,100):
    for j in range(0,100):
        if((i+1)%(j+1)==0):
            if(n[i]==0):
                n[i]=1
            else:
                n[i]=0
    #print(n,end="\n==>\n")
print("Count of doors opened",n.count(1))
print(n)