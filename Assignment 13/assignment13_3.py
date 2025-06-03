class Numbers:
    def __init__(self,A):
        self.value = A

    def ChkPrime(self):
        val = self.value
        counter = 0
        for i in range(1,val+1):
            if val%i == 0:
                counter = counter + 1
        
        if counter == 2:
            return True
        else : 
            return False

    def ChkPerfect(self):
        val = self.value
        num = 0
        for i in range(1,val):
            if val%i == 0:
                num = num + i
            
        if num == val:
            return True
        else:
            return False

    def SumFactors(self,values):
        sum = 0
        for i in values:
            sum = sum + i

        return sum

    def Factors(self):
        print("Factors of ",self.value," are : ")
        val = self.value
        demo = []
        for i in range(1,val+1):
            if val%i == 0:
                print(i)
                demo.append(i)
        
        return demo

def main():
    print("Enter a Number : ")
    No = int(input())
    obj = Numbers(No)

    Demo = []

    ret = obj.ChkPrime()
    if ret == True:
        print("Number is a Prime Number")
    else:
        print("Number is not a Prime Number")

    ret = obj.ChkPerfect()
    if ret == True:
        print("Number is a Perfect Number")
    else:
        print("Number is not a Perfect Number")

    Demo = obj.Factors()

    sum = obj.SumFactors(Demo)
    print("Sum of all the factors is : ",sum)

if __name__ == "__main__":
    main()