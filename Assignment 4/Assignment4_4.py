even = lambda x : x%2 == 0
sqre = lambda x : x*x
add = lambda x,y : x+y

def filterX(func,values):
    temp = []
    for i in values:
        ret = func(i)
        if ret == True:
            temp.append(i)
    
    return temp

def mapX(func,values):
    temp = []
    for i in values:
        ret = func(i)
        temp.append(ret)

    return temp

def reduceX(func,values):
    temp = 0
    for i in values:
        temp = func(temp,i)

    return temp

def main():
    print("Enter the length of the list :")
    length = int(input())

    Demo = []

    print("Enter the elements :")
    for i in range(length):
        val = int(input())
        Demo.append(val)

    Fdemo = list(filterX(even,Demo))

    print("List after filter : ",Fdemo)

    Mdemo = list(mapX(sqre,Fdemo))

    print("List after map :",Mdemo)

    Rdata = reduceX(add,Mdemo)

    print("Output of reduce : ",Rdata)


if __name__ == "__main__":
    main()