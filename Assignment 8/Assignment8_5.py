import threading

def displayNormal(val):
    for i in range(1,val+1):
        print(i)


def displayReverse(val):
    for i in range(val,-1,-1):
        print(i)

def main():

    x = 50
    Thread1 = threading.Thread(target=displayNormal,args=(50,))
    Thread1.start()
    Thread1.join()

    Thread2 = threading.Thread(target=displayReverse,args=(50,))
    Thread2.start()
    Thread2.join()

if __name__ == "__main__":
    main()