mult = lambda x,y : x*y

def main():
    print("Enter first number :")
    No1 = int(input())

    print("Enter second number :")
    No2 = int(input())

    res = mult(No1,No2)

    print("Multiplication of ",No1," and ",No2," is : ",res)

if __name__ == "__main__":
    main()