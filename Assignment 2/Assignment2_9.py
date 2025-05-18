def main():
    print("Enter a number :")
    No = int(input())
    
    counter = 1
    while int(No/10) != 0:
        val = int(No/10)
        No = val
        counter = counter + 1
        
    print(counter)

if __name__ == "__main__":
    main()