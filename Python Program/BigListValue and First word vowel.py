# defining the function 
def makeBigList(userList,lowerBound):
    # new list
    newList = []
    for i in userList:
        # checking the bigger value
        if(i>lowerBound):
            # appending the values
            newList.append(i)
    # returing the list
    return newList

# uncomment the below 2 lines, if you want to take
# values form user
# userList = [int(n) for n in input().split()]
# lowerBound = int(input())

# change the values below to test for another parameters
userList = [5,4,3,2,1]
lowerBound = 2
# sorting the list
sortedList = makeBigList(userList,lowerBound)
sortedList.sort()
# displaying the result
print(sortedList)

# defining the function
def countVowelWords(userStringList):
    # count variable
    count = 0
    # iterating over the loop
    for i in userStringList:
        # checking the first letter contains the vowels
        if(i.upper()[0] in ['A','E','I','O','U']):
            # incrementing the count
            count+=1
    # returing the count
    return count

# getting input form user
userString = input()
# spliting the string as list of words
userStringList = userString.split()
# displaying the result
print("The total words which starts with vowels are", countVowelWords(userStringList))

