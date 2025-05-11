def main():                     # here main function body is written
    print("Enter a Number :")   # here code ask for user input
    no = int(input())           # here code type cast user input into integer as input function consider all values bydefault string and store it into no variable

    if no%5 == 0:               # here code check if user input which store into no is divisle by 5 or not with if statement 
        print("True")           # here code print "True" if condition return True
    else:                       # here if above condition return False then else statement get executed
        print("False")          # here code print "False"

if __name__ =="__main__":       # code start from here
    main()                      # main function get call from here and code jump to line 1  