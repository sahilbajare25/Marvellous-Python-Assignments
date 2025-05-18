def main():
    print("Enter a number :")
    No = int(input())
    counter = 0

    for i in range(No+1):
        
        if i == 0:
            continue 
         
        if No % i == 0:
            counter = counter + 1
        
    if counter == 2 :
        print("It is a Prime Number")
    else:
        print("It is not a Prime Number")

if __name__ == "__main__":
    main()