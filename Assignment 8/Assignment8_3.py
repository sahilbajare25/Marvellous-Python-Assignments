import threading

def displayEven(values):
    print("Even elements from the list are ")
    sum = 0
    for i in values:
        if i%2 == 0:
            print(i)
            sum = sum + i
    
    print("Sum of even elements from the list is : ",sum)


def displayOdd(values):
    print("odd elements from the list are ")
    sum = 0
    for i in values:
        if i%2 != 0:
            print(i)
            sum = sum + i
    
    print("Sum of odd elements from the list is : ",sum)
    

def main():

    print("Enter length of list : ")
    No = int(input())

    Demo = []

    print("Enter elements in the list")
    for i in range(No):
        val = int(input())
        Demo.append(val)

    evenfactor = threading.Thread(target=displayEven,args=(Demo,))
    evenfactor.start()
    evenfactor.join()

    oddfactor = threading.Thread(target=displayOdd,args=(Demo,))
    oddfactor.start()
    oddfactor.join()


if __name__ == "__main__":
    main()