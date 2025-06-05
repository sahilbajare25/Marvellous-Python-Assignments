class Calculator:
    def __init__(self,A,B):
        self.No1 = A
        self.No2 = B

    def Add(self):
        return (self.No1 + self.No2)
    
    def Subtract(self):
        return (self.No1 - self.No2)
    
    def Multiply(self):
        return (self.No1 * self.No2)
    
    def Divide(self):
        return (self.No1 / self.No2)

def main():
    print("Enter the first number : ")
    No1 = int(input())

    print("Enter the second number : ")
    No2 = int(input())

    obj = Calculator(No1,No2)

    res = obj.Add()
    print("Addition is : ",res)

    res = obj.Subtract()
    print("Subtraction is : ",res)

    res = obj.Multiply()
    print("Multiplication is : ",res)

    res = obj.Divide()
    print("Division is : ",res)

if __name__ == "__main__":
    main()