# defining the fundamentalPeriod function
def fundamentalPeriod(userinput):
        # getting length
        userInputLength = len(userinput)
        periodDefine = 0
        i = 0
        # looping over the userinput from current 
        # next position
        for j in range(1,userInputLength):
                characterPresent = userinput[j]
                characterNext = userinput[i]
                if (characterPresent == characterNext):
                    periodDefine = (j - i)
                    i += 1
                else:
                    if (characterPresent == userinput[0]):
                        i = 1
                        periodDefine = j
                    else:
                        i = 0
                        periodDefine = 0
        if periodDefine==-1 or userInputLength%periodDefine!=0:
            return 0
        periodDefine="period"
        return periodDefine
# getting value from user
userInput=input()
# displaying the result
print(fundamentalPeriod(userInput))