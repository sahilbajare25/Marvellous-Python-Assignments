from functools import reduce

even = lambda x : x%2 == 0

square = lambda x : x*x

add = lambda x,y : x+y

def main():

    print("Enter the length of list :")
    length = int(input())

    Demo = []

    print("Enter  the elements : ")
    for i in range(length):
        val = int(input())
        Demo.append(val)

    Fdemo = list(filter(even,Demo))

    print("List after filter : ",Fdemo)

    Mdemo = list(map(square,Fdemo))

    print("List after map : ",Mdemo)

    Rdata = reduce(add,Mdemo)

    print("Output of reduce : ",Rdata)

if __name__ == "__main__":
    main()