# defining the global varibale
PI = 3.14
# defining the function shape
def shapes(shapeName, shapeSize):
    # function to get area of circle
    def areaCircle(shapeSize):
        area = PI * shapeSize * shapeSize
        return area
    # function to get area of Square                                                                                                                                                                                                                                                                                                                            
    def areaSquare(shapeSize):
        area = shapeSize * shapeSize
        return area
    # checking the shape entered is circle or not
    if(shapeName=='circle'):
        # displaying the result
        print("The circle area is ", areaCircle(shapeSize))
        exit();
    # checking the shape entered is circle or not
    if(shapeName=='square'):
        # displaying the result
        print("The square area is ", areaSquare(shapeSize))
        exit();
        
# getting the inputs from user
shapeName, shapeSize = input().split()
# converting the shape into lower case
shapeName = shapeName.lower()
# converting the string type shape size to integer
shapeSize = int(shapeSize)
# calling the main function
print(shapes(shapeName,shapeSize))


