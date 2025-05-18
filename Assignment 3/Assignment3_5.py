import MarvellousNum

def ListPrime(LDemo):
    Add = 0 
    for i in LDemo:
       
        num = MarvellousNum.ChkPrime(i)
        if num == True:
            Add = Add + i
            #print(i)
        
    
    print("Addition of elements is : ",Add)


def main():
    print("Enter the number of elements :")
    No = int(input())

    Demo = list()

    print("Enter  the elements : ")
    for i in range(No):
        val = int(input())
        Demo.append(val)

    ListPrime(Demo)



if __name__ == "__main__":
    main()