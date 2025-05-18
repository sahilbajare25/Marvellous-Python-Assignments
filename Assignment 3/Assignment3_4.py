def main():
    print("Enter the length of list :")
    No = int(input())

    Demo = list()

    print("Enter  the elements : ")
    for i in range(No):
        val = int(input())
        Demo.append(val)
    
    print("Element to search : ")
    element = int(input())

    counter = 0

    for i in Demo:
        if i == element:
            counter = counter + 1

    print("frequency of element ",element," in list is : ",counter) 

if __name__ == "__main__":
    main()