class Rectangle:
    def __init__(self,A,B):
        self.length = A
        self.width = B

    def calculateArea(self):
        return (self.length * self.width)
    
    def calculatePerimeter(self):
        return (2 * (self.length + self.width))

def main():
    print("Enter length of rectangle : ")
    length = int(input())
    print("Enter width of rectangel : ")
    width = int(input())

    obj = Rectangle(length,width)
    
    res = obj.calculateArea()
    print("Area of rectagle is : ",res)

    res = obj.calculatePerimeter()
    print("Perimeter of rectangle is : ",res)


if __name__ == "__main__":
    main()