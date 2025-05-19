#use reduce() function to print product of all numbers

mult = lambda x,y : x*y

def reduceX(func,values):
    temp = 1
    for i in values:
        temp = func(temp,i)

    return temp

def main():
    print("Enter lenght of list :")
    length = int(input())

    Demo = []

    print("Enter the elements : ")
    for i in range(length):
        no = int(input())
        Demo.append(no)

    rdata = reduceX(mult,Demo)

    print("Product : ",rdata)



if __name__ == "__main__":
    main()