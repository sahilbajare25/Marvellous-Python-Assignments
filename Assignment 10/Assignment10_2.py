# write lambda function which return multiplication of two number

multi = lambda x,y : x*y

def main():
    print("Enter First number :")
    No1 = int(input())

    print("Enter Second number :")
    No2 = int(input())

    ret = multi(No1,No2)

    print("Multiplication is : ",ret)

if __name__ == "__main__":
    main()