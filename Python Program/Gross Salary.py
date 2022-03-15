rate = 15
baseSalary = float(input("Enter the base salary: "))
hours = float(input("Enter the hours worked: "))
if(hours>=55):
    grossSalary = (hours-55)*rate*1.5+baseSalary
elif(hours>=35 and hours<55):
    grossSalary = hours*rate + baseSalary
else:
    grossSalary = baseSalary
print(f"The Gross Salary is: {grossSalary:.2f}")
    
