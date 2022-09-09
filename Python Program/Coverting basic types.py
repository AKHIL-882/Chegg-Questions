# getting user inputs
user_input1 = int(input("Enter integer:\n"))
user_input2 = float(input("Enter double:\n"))
user_input3 = input("Enter character:\n")
user_input4 = input("Enter string:\n")
ar = []
# appending to array
ar.append(user_input1)
ar.append('%.6f' % user_input2)
ar.append(user_input3)
ar.append(user_input4)
# displaying the result
for i in ar:
    print(i,end=" ")
print('\n')
for i in ar[::-1]:
    print(i,end=" ")
print('\n')
print(ar[1],"cast to an integer is", int(user_input2))
