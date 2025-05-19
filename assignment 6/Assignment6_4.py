#Factorial

def main():
    print("Enter a number : ")
    no = int(input())
    fact = 1

    for i in range(1,no+1):
        fact = fact * i
    
    print("Factorial of ",no," is : ",fact)

if __name__ == "__main__":
    main()