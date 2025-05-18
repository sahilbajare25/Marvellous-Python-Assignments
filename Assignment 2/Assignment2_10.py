def main():
    print("Enter a number :")
    No = int(input())
    add = 0
    
    while int(No/10) != 0:
        val = int(No/10)
        num = int(No%10)
        add = add + num
        No = val

    add = add + No    
    print("Addition of the digit in number is : ",add)

if __name__ == "__main__":
    main()