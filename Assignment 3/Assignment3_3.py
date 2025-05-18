def main():
    print("Enter the length of list :")
    No = int(input())

    Demo = list()

    print("Enter  the elements : ")
    for i in range(No):
        val = int(input())
        Demo.append(val)

    min = Demo[0]
    
    for i in Demo:
        if i < min:
            min = i

    print("Minimum element in list is : ",min) 

if __name__ == "__main__":
    main()