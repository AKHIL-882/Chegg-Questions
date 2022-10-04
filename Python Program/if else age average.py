
# function declaration
def AverageAge(n):
    # displaying the average
    print("The average age of these " + str(len(n)) + " members is " + str(sum(n)/len(n)))
     
# list to store age
data = [] 
# getting the count of members
n = int(input("Please enter the number of people in the group: "))
# getting values from user
# appending the values into list
for i in range(n):
    data.append(int(input("Enter the age of a member: ")))
# function calling
AverageAge(data)
















# function declaration
def AverageAge(n):
    if n>=21:
        return True
    else:
        return False 
            
# list to store age
data = [] 
count = 0
# getting the count of members
n = int(input("Please enter the number of people in the group: "))
# getting values from user
# appending the values into list
for i in range(n):
    v = int(input("Enter the age of a member: "))
    data.append(v)
    if(AverageAge(v)):
        count = count + 1
        print("This is an adult.")
    else:
        print("This is not an adult.")
print("The average age of these " + str(len(data)) + " members is " + str(sum(data)/len(data)) + ".")
print("The group has " + str(count) + " adult(s).")




