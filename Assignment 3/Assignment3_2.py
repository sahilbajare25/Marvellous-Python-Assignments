def main():
    print("Enter the length of list :")
    No = int(input())

    Demo = list()
    max = 0

    print("Enter  the elements : ")
    for i in range(No):
        val = int(input())
        Demo.append(val)
    
    for i in Demo:
        if i > max:
            max = i

    print("Maximum element in list is : ",max) 

if __name__ == "__main__":
    main()