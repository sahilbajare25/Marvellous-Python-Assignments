def main():
    print("Enter the length of list :")
    No = int(input())

    Demo = list()
    Add = 0

    print("Enter  the elements : ")
    for i in range(No):
        val = int(input())
        Demo.append(val)
    
    for i in Demo:
        Add = Add + i

    print("Addition of all the elements in list is : ",Add) 

if __name__ == "__main__":
    main()