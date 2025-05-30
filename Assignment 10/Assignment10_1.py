# write lambda function which returns power of 2

power = lambda x : 2**x

def main():
    print("Enter the number :")
    No = int(input())

    ret = power(No)

    print(ret)

if __name__ == "__main__":
    main()