def main():                     # here main function body is written
    print("Enter a number :")   # here code ask for user input
    no = int(input())           # here code type cast user input into integer as input function consider all values bydefault string and store it into no variable

    i = 0                       # here one local variable is taken and initiated with 0 value as counter 
    while i<no:                 # here while loop is used to check whether i is leass that user input or not
        print("*", end=" ")     # here code get inside while loop if return True and print * and end="" is used to print value on same line
        i = i+1                 # here i variable is incremented by 1


if __name__ == "__main__":      # code start from here
    main()                      # main function get call from here and code jump to line 1 