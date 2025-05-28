import threading

def displayOdd():
    print("Odd number :")
    for i in range(1,20,2):
        print(i)


def displayEven():
    print("Even Numbers : ")
    for i in range(2,21,2):
        print(i)

def main():

    even = threading.Thread(target=displayEven)
    even.start()

    odd = threading.Thread(target=displayOdd)
    odd.start()

if __name__ == "__main__":
    main()