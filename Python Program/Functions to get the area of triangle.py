# function to get height
def getHeight(height):
    return float(height)
# function to get base
def getBase(base):
    return float(base)
# function to get area
def getArea(base,height):
    return float(base*height*.5)
# function to display data
def displayData(base,height,area):
    print("\nTriangle's Area\n-----------------")
    print("Base:\t",base)
    print("Height:\t",height)
    print("Area:\t",round(area,2))
# getting inputs and calling function
height = getHeight(input("Enter the triangle's base: "))
base = getHeight(input("Enter the triangle's height: "))
area = getArea(height,base)
displayData(base,height,area)
    
