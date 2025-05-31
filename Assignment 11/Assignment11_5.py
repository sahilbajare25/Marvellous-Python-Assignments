'''count = 0

def displayCount(val):
    global count

    if int(val/10) != 0:
        num = val%10
        if num == 0:
            count = count + 1
        val = int(val/10)
        displayCount(val)
    
    return count'''

def displayCount(val):
    count = 0
    while int(val/10) != 0:
        num = val%10
        if num == 0:
            count = count + 1
        
        val = int(val/10)
        #print(val)
        displayCount(val)
    
    if val == 0:
            count = count + 1

    return count

def main():
    print("Enter a Number : ")
    no = int(input())

    ret = displayCount(no)

    print("Number of Zeros are : ",ret)

if __name__ == "__main__":
    main()