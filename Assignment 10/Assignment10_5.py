def chkPrime(val):
    counter = 0
    for i in range(1,val+1):
        if val%i == 0:
            counter = counter + 1
                
    if counter == 2:
        return True
    else:
        return False
    
multi = lambda x : x*2
            
def maximum(no1,no2):
    if no1 > no2:
        return no1
    else : 
        return no2

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
    print("Enter the length of list :")
    length = int(input())

    Demo = []

    print("Enter  the elements : ")
    for i in range(length):
        val = int(input())
        Demo.append(val)

    Fdemo = list(filterX(chkPrime,Demo))

    print("List after filter : ",Fdemo)

    Mdemo = list(mapX(multi,Fdemo))

    print("List after map : ",Mdemo)

    Rdata = reduceX(maximum,Mdemo)

    print("Output of reduce : ",Rdata)

if __name__ == "__main__":
    main()