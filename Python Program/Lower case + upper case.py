n = int(input())
userString = []
for i in range(n):
    userVal = input()
    userString.append(userVal)
lowerCase= ""
upperCase = ""

for i in userString:
    for j in i:
        if j.islower():
            lowerCase= lowerCase + j
        else:
            upperCase = upperCase + j
    print(lowerCase+upperCase)
    lowerCase,upperCase = "",""
    
    
    
