compare = lambda x : x >= 70 and x <= 90
add = lambda x : x+10
mult = lambda x,y : x*y

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
    temp = 1
    for i in values:
        temp = func(temp,i)
    
    return temp


def main():
    print("Enter the length of list :")
    length = int(input())

    Demo = list()

    print("Enter the elements :")
    for i in range(length):
        val = int(input())
        Demo.append(val)

    Fdemo = list(filterX(compare,Demo))

    print("List after filter : ",Fdemo)

    Mdemo = list(mapX(add,Fdemo))

    print("List after map :",Mdemo)

    Rdata = reduceX(mult,Mdemo)

    print("Output of reduce : ",Rdata)

if __name__ == "__main__":
    main()