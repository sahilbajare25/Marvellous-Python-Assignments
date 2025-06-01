class Circle:
    PI = 3.14

    def __init__(self,A,B,C):
        self.Radius = A
        self.Area = B
        self.Circumference = C

    def Accept(self,A):
        self.Radius = A

    def CalculateArea(self):
        self.Area = Circle.PI * self.Radius * self.Radius

    def CalculateCircumference(self):
        self.Circumference = 2 * Circle.PI * self.Radius

    def display(self):
        print("Radius of Circle is : ",self.Radius)
        print("Area of Circle is : ",self.Area)
        print("Circumference of Circle is : ",self.Circumference)

def main():

    obj = Circle(0.0,0.0,0.0)
    obj.Accept(4)
    obj.CalculateArea()
    obj.CalculateCircumference()
    obj.display()
    
    obj.Accept(6)
    obj.CalculateArea()
    obj.CalculateCircumference()
    obj.display()
    
if __name__ == "__main__":
    main()