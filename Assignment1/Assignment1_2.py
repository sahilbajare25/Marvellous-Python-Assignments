def ChkNum():                   # program enter into ChkNum function
    print("Enter a number :")   # here code ask for user input
    No = int(input())           # here code store the user input inside No variable

    if No%2 == 0:               # here code checks if user input number is divisible by 2 or not
        print("Even Number")    # here code enter if the number is divisible by 2 and print "Even Number"
    else:
        print("Odd Number")     # here code enter if the number is not divisible by 2 and print "Odd Number"


if __name__ == "__main__":      # Code start from line 11
    ChkNum()                    # From line 12 program jump to line 1