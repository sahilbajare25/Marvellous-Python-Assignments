# find the largest among three numbers 

def maximum(val1,val2,val3):
    if val1 > val2 and val1 > val3:
        return val1
    elif val2 > val1 and val2 > val3:
        return val2
    else :
        return val3

def main():
    print("Enter three number :")
    no1 = int(input())
    no2 = int(input())
    no3 = int(input())

    ret = maximum(no1,no2,no3)

    print("Largest number is : ",ret)

if __name__ == "__main__":
    main()