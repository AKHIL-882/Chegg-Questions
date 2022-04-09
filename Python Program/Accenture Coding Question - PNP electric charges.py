userInput = [int(n) for n in input().split()]
userString = input()
userNumber = int(input())
sum = 0
for i in range(len(userString)):
    if(userString[i]=="P"):
        sum = sum + userInput[i]
    elif(userString[i]=="N"):
            sum = sum - userInput[i]
print(sum*100)
        