#Arithmetic Operation on Two Numbers

def addition(val1,val2):
    return val1+val2

def subtraction(val1,val2):
    return val1-val2

def multiplication(val1,val2):
    return val1*val2

def division(val1,val2):
    return val1/val2

def main():
    print("Enter first number : ")
    no1 = int(input())

    print("Enter Second number : ")
    no2 = int(input())

    add = addition(no1,no2)
    sub = subtraction(no1,no2)
    mult = multiplication(no1,no2)
    div = division(no1,no2)

    print("Sum is : ",add)
    print("Difference is : ",sub)
    print("Product is : ",mult)
    print("Division is : ",div)

if __name__ == "__main__":
    main()