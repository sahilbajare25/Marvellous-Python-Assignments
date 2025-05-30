import functools

def select(no):
    return(no >= 70 and no <= 90)

def increase(no):
    return(no+10)

def multi(no1,no2):
    return(no1*no2)

def main():

    print("Enter the length of list :")
    length = int(input())

    Demo = []

    print("Enter  the elements : ")
    for i in range(length):
        val = int(input())
        Demo.append(val)

    Fdemo = list(filter(select,Demo))

    print("List after filter : ",Fdemo)

    Mdemo = list(map(increase,Fdemo))

    print("List after map : ",Mdemo)

    Rdata = functools.reduce(multi,Mdemo)

    print("Output of reduce : ",Rdata)


if __name__ == "__main__":
    main()