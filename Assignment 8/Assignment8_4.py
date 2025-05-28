import threading

def displaySmall(value):

    print("Small characters in the string are :")
    
    x = 0
    for i in value:
        x = ord(i)
        if x >= 97 and x <=122:
            print(i)
    
    print("Thread id of child thread is : ",threading.get_ident())

def displayCapital(value):

    print("Capital characters in the string are :")
    
    x = 0
    for i in value:
        x = ord(i)
        if x >= 65 and x <=90:
            print(i)

    print("Thread id of child thread is : ",threading.get_ident())

def displayDigit(value):

    print("Digits in the string are :")
    
    x = 0
    for i in value:
        x = ord(i)
        if x >= 48 and x <=57:
            print(i)

    print("Thread id of child thread is : ",threading.get_ident())
        
def main():
    print("Enter a string : ")
    var = input()

    print("Thread id of main thread is : ",threading.get_ident())

    small = threading.Thread(target=displaySmall,args=(var,))
    small.start()
    small.join()

    capital = threading.Thread(target=displayCapital,args=(var,))
    capital.start()
    capital.join()

    digit = threading.Thread(target=displayDigit,args=(var,))
    digit.start()
    digit.join()


if __name__ == "__main__":
    main()