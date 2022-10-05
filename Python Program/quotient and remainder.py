# function declaration
def quotientRemainder(firstNumber, secondNumber):
    # calculating the quotient
    q = firstNumber//secondNumber
    print("The quotient is: ", q)
     
    # calculating the remainder
    r = firstNumber%secondNumber
    print("The remainder is: ", r)
# getting input from user
firstNumber = int(input())
secondNumber = int(input())
# function calling
quotientRemainder(firstNumber,secondNumber)
