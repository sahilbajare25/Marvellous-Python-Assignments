sum = 0

def Addition(val):
    #print(val,"% 10 : ",val%10," ",val," / 10 is :", int(val/10))
    global sum
    if int(val/10) != 0:
        num = val%10
        sum = sum + num
       
        val = int(val/10)
        Addition(val)
    else:
        sum = sum + val
    
    #print(val)
    #sum = sum + val
    return sum

def main():
    print("Enter a number : ")
    no = int(input())

    ret = Addition(no)

    print("Sum of Digits ",no," is : ",ret)

if __name__ == "__main__":
    main()