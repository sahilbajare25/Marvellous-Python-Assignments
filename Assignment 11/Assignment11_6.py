sum = 0

def Addition(val):
    global sum
    if val >= 1:
        sum = sum + val
        val = val - 1
        Addition(val)

    return sum

def main():
    print("Enter a Number : ")
    No = int(input())

    ret = Addition(No)

    print("The sum is : ",ret)

if __name__ == "__main__":
    main()