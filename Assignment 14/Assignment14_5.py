class BankAccount:
    def __init__(self,A,B,C):
        self.Account_number = A
        self.Name = B
        self.Balance = C

    def display(self):
        print("Account details : ")
        print("Name : ",self.Name)
        print("Account Number : ",self.Account_number)
        print("Account Balance : ",self.Balance)

    def depositAmount(self,amount):
        self.Balance = self.Balance + amount
        print("Account balannce after amount deposit is : ",self.Balance)

    def withdrawAmount(self,amount):
        self.Balance = self.Balance - amount
        print("Account balannce after amount withdraw is : ",self.Balance)
        


def main():
    print("Enter the Name of Account Holder : ")
    Name = input()
    print("Enter the Account number :")
    accountNumber = int(input())
    print("Enter the Account balance : ")
    Balance = int(input())

    obj = BankAccount(accountNumber,Name,Balance)

    obj.display()

    obj.depositAmount(500)

    obj.withdrawAmount(2100)

if __name__ == "__main__":
    main()