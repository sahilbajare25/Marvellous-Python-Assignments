class Employee:
    def __init__(self,A,B,C):
        self.Name = A
        self.emp_id = B
        self.salary = C

    def display(self):
        print("Employees Details :")
        print("Name : ",self.Name)
        print("Id : ",self.emp_id)
        print("Salary : ",self.salary)

def main():
    print("Enter name of employee : ")
    Name = input()
    print("Enter employee id :")
    Id = int(input())
    print("Enter salary of employee : ")
    Salary = int(input())

    obj = Employee(Name,Id,Salary)
    obj.display()

if __name__ == "__main__":
    main()