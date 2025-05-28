import multiprocessing

def factorial(val):
    fact = 1
    for i in range(val,0,-1):
        fact = fact * i
    
    return fact

def main():

    print("Enter the length of list :")
    length = int(input())

    Demo = []

    print("Enter the elements : ")
    for i in range(length):
        val = int(input())
        Demo.append(val)

    NewDemo = []

    p = multiprocessing.Pool()

    res = p.map(factorial,Demo)
    
    p.close()

    print("Factorial are :")
    print(res)

if __name__ == "__main__":
    main()