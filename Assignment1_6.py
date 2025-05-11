def main():                         # here main function body is written
    print("Enter a number :")       # here code ask for user input
    no = int(input())               # here code type cast user input into integer as input function consider all values bydefault string and store it into no variable
    
    if no > 0:                      # here user input value which store into no is check with if statement whether the value is greater than 0 or not 
        print("Positive Number")    # here code print "Postive Number" if condition return True
    elif no < 0:                    # here user input value which store into no is check with elif statement whether the value is lesser than 0 or not 
        print("Negative Number")    # here code print "Negative Number" if condition return True
    else:                           # here if above both condition return False then code enter else statement
        print("Zero")               # here code print "Zero"


if __name__ == "__main__":          # code start from here
    main()                          # main function get call from here and code jump to line 1              