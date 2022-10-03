firstServiceCost=0
secondServiceCost=0


print("Davy's auto shop services")
print("Oil change -- $35")
print("Tire rotation -- $19")
print("Car wash -- $7")
print("Car wax -- $12")

#print("\nSelect first service:")
print()
firstService=input("Select first service: ")
#print("Select second service:")
secondService=input("Select second service: ")


if firstService=="Oil change":
    firstServiceCost=35


if firstService=="Tire rotation":
    firstServiceCost=19

if firstService=="Car wash":
    firstServiceCost=7


if firstService=="Car wax":
    firstServiceCost=12


if firstService=="-":
    firstService="No service"
    secondServiceCost=35
    
    
    

if secondService=="Tire rotation":
    secondServiceCost=19


if secondService=="Car wash":
    secondServiceCost=7

if secondService=="Car wax":
    secondServiceCost=12

if secondService=="-":
    secondService="No service"

totalCost=firstServiceCost+secondServiceCost;

print("\nDavy's auto shop invoice")
print("\nService 1:",firstService,end="")

if firstService!="No service":
    print(", $"+str(firstServiceCost))
    print("Service 2:",secondService,end="")
    print("\n\nTotal: $"+str(totalCost))

if secondService!="No service":
    print()
    print("Service 2: "+ secondService + ", " + '$'+ str(secondServiceCost))
    print("\nTotal: $"+str(totalCost))
    
    
    
    
    