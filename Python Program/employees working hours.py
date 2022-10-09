
# local variables
sum_ = 0
sumAll = []
# getting data of two Employees
for i in range(1,3):
    print("Employee",i,": How many days? ",end="")
    # getting the number of days from user
    e1 = int(input())
    # iterating over the value
    for i in range(e1):
        # getting hours data from user
        hours = int(input("Hours? "))
        # adding the hours
        sum_ = sum_ + hours
    # appending hours to list
    sumAll.append(sum_)
    # displaying individual result
    print("Employee 1's total hours =", sum_ , round(sum_/e1,2))
    # setting sum_=0
    sum_=0
# displaying the total hours spent
print("Total hours for both",sum(sumAll))