class BankAccount:

    ROI = 10.5 

    def __init__(self,A,B):
        self.Name = A
        self.Amount = B

    def Display(self):
        print("Name of account holder is : ",self.Name)
        print("Current Amount in account is : ",self.Amount)

    def Deposit(self,value):
        self.Amount = self.Amount + value
        print("Current amount in the account is : ",self.Amount)

    def Withdraw(self,value):
        self.Amount = self.Amount - value
        print("Current amount in the account is : ",self.Amount)

    def CalcuateIntrest(self):
        RateOfInterest = 0
        RateOfInterest = (self.Amount * BankAccount.ROI)/ 100
        return RateOfInterest


def main():

    print("Enter the Name of Account holder : ")
    Name = input()
    print("Enter the Amount : ")
    Amount = int(input())

    obj = BankAccount(Name,Amount)

    obj.Display()

    print("Enter the amount to deposit : ")
    AmountDeposit = int(input())
   
    obj.Deposit(AmountDeposit)

    print("Enter the amount to Withdraw")
    AmountWithdraw = int(input())
    obj.Withdraw(AmountWithdraw)
    FinalAmount = obj.CalcuateIntrest()
    print("Rate of Interest is : ",FinalAmount)

if __name__ == "__main__":
    main()