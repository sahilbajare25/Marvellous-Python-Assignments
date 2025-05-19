# prime number

def main():
    print("Enter a number : ")
    no = int(input())
    counter = 0

    for i in range(1,no+1):
        if no%i == 0:
            counter = counter + 1
    
    if counter == 2:
        print(no," is a prime number")
    else:
        print(no," is not a prime number")

if __name__ == "__main__":
    main()