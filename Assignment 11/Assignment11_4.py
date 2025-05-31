res = 1

def calculate(val,power):
    global res
    i = 1
    if i <= power:
        res = res * val
        power = power-1
        calculate(val,power)

    return res

def main():
    print("Enter the number : ")
    no = int(input())

    print("Enter the power : ")
    power = int(input())

    ret = calculate(no,power)

    print("The Result is : ",ret)

if __name__ == "__main__":
    main()