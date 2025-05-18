import Arithmetic

def main():
    print("Enter first number : ")
    No1 = int(input())

    print("Enter second number : ")
    No2 = int(input())

    Addition = Arithmetic.Add(No1,No2)
    Subtraction = Arithmetic.Sub(No1,No2)
    Multiplication = Arithmetic.Mult(No1,No2)
    Division = Arithmetic.Div(No1,No2)

    print("Addition is : ",Addition)
    print("Subtraction is : ",Subtraction)
    print("Multiplication is : ",Multiplication)
    print("Division is : ",Division)

if __name__ == "__main__":
    main()