class Artihmetic:

    def __init__(self,A,B):
        self.value1 = A
        self.value2 = B

    def Accept(self,A,B):
        self.value1 = A
        self.value2 = B

    def Addition(self):
        return self.value1 + self.value2

    def Subtraction(self):
        return self.value1 - self.value2

    def Multiplication(self):
        return self.value1 * self.value2

    def Division(self):
        return self.value1 / self.value2

def main():

    obj = Artihmetic(0,0)
    obj.Accept(12,2)
    res = obj.Addition()
    print("Addition is : ",res)
    res = obj.Subtraction()
    print("Subtraction is : ",res)
    res = obj.Multiplication()
    print("multiplication is : ",res)
    res = obj.Division()
    print("Division is : ",res)

    obj.Accept(18,3)
    res = obj.Addition()
    print("Addition is : ",res)
    res = obj.Subtraction()
    print("Subtraction is : ",res)
    res = obj.Multiplication()
    print("multiplication is : ",res)
    res = obj.Division()
    print("Division is : ",res)

if __name__ == "__main__":
    main()