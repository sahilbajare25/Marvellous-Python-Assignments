#Use map() function to double each value

double = lambda x : x*2

def mapX(func,values):
    temp = []
    for i in values:
        ret = func(i)
        temp.append(ret)

    return temp

def main():
    print("Enter lenght of list :")
    length = int(input())

    Demo = []

    print("Enter the elements : ")
    for i in range(length):
        no = int(input())
        Demo.append(no)

    Mlist = list(mapX(double,Demo)) 

    print("Doubled list : ",Mlist)


if __name__ == "__main__":
    main()