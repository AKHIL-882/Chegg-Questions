count1=0
count2=0
userInput1 = input().lower()
userInput2 = input().lower()
charRead = input().lower()
for i in range(len(userInput1)):
    if(userInput1[i]==charRead):
        count1 = count1+1
for i in range(len(userInput2)):
    if(userInput2[i]==charRead):
        count2= count2+1
if(count1<count2):
    print(userInput2)
    print(count2)
elif(count1==count2):
    print("Both strings have same frequency of given character")
    print(count1)
else:
    print(userInput1)
    print(count1)
    
