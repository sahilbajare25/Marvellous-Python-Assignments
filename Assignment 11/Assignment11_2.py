res = 1

def factorial(val):
    global res
    if val >= 1:
        res = res * val
        val = val - 1
        factorial(val)
    
    return res

def main():
    print("Enter a number : ")
    no = int(input())

    ret = factorial(no)

    print("Factorial of ",no," is : ",ret)

if __name__ == "__main__":
    main()