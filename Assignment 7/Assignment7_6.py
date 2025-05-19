#use filter() function to print prime numbers

def prime(val1):
    counter = 0

    if val1 == 1:
        return True
    
    for i in range(1,val1+1):
        if val1%i == 0:
            counter = counter + 1
    
    if counter == 2:
        return True
    else : 
        return False


def filterX(func,values):
    temp = []
    for i in values:
        ret = func(i)
        if ret == True:
            temp.append(i)

    return temp

def main():
    print("Enter lenght of list :")
    length = int(input())

    Demo = []

    print("Enter the elements : ")
    for i in range(length):
        no = int(input())
        Demo.append(no)

    Flist = list(filterX(prime,Demo))

    print("Prime numbers : ",Flist)


if __name__ == "__main__":
    main()