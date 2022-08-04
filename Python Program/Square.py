class Square:
    name = "Square"
    
    def __init__(self,side):
        self.side = side
        
    def area(self):
        x=self.side
        a=x*x
        print("The area is:",a)
    def perimeter(self):
        x = self.side
        p=x*4
        print("Perimeter is:",p)
mySquare = Square(2)
mySquare.area()
mySquare = Square(2)
mySquare.perimeter()