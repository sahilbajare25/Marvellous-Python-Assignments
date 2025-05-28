import threading

def displayEven(val):
    print("Even factors of ",val," are")
    sum = 0
    for i in range(1,val+1):
        if val%i == 0:
            if i%2 == 0:
                print(i)
                sum = sum + i
    
    print("Sum of even factors of ",val," is : ",sum)

def displayOdd(val):
    print("Odd factors of ",val," are")
    sum = 0
    for i in range(1,val+1):
        if val%i == 0:
            if i%2 != 0:
                print(i)
                sum = sum + i
    
    print("Sum of odd factors of ",val," is : ",sum)


def main():

    print("Enter a number : ")
    No = int(input())

    evenfactor = threading.Thread(target=displayEven,args=(No,))
    evenfactor.start()
    evenfactor.join()

    oddfactor = threading.Thread(target=displayOdd,args=(No,))
    oddfactor.start()
    oddfactor.join()

    print("Exit from main")


if __name__ == "__main__":
    main()