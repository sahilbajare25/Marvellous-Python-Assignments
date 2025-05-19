#use filter() function to keep only even numbers

even = lambda x : x%2 == 0

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

    Flist = list(filterX(even,Demo))

    print("Even numbers : ",Flist)


if __name__ == "__main__":
    main()