def Add(val1,val2):                     # here Add function body is written with two local variables val1,val2 is taken to store values passed while function call
    ans = val1+val2                     # here one local variable is taken "ans" to store the addition value of val1 and val2
    return ans                          # here the ans value is return and code jump to line 12

def main():                             # here main function body is written
    print("Enter first Number :")       # here code ask for user input
    No1 = int(input())                  # here code store the user input inside No1 variable

    print("Enter Second Number :")      # here code ask for second user input
    No2 = int(input())                  # here code store the user input inside No2 variable

    res = Add(No1,No2)                  # here Add function get call and while calling No1 and No2 user input is passed and return value is store into res variable and code jump to line 1

    print(res)                          # here res value get printed

if __name__ == "__main__":              # Code start from line 16
    main()                              # Here main function get call and code jump to line 5