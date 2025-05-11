def main():                     # here main function body is written
    i = 1                       # here local variable i is taken and stored with 1 value
    count = 0                   # here local variable count is taken and stored with 0 value for counter
    while count < 10:           # here while loop is used to check whether count is less that 10 or not
        if i%2 == 0:            # here code gets inside while loop if return True and then check if i is divisble by 2 or not 
            print(i, end=" ")   # here code gets inside if statement if returns True amd print i value
            count = count + 1   # here count variable is incremented by 1
        i = i + 1               # here i variable is incremented by 1
            
if __name__ == "__main__":      # code start from here
    main()                      # main function get call from here and code jump to line 1