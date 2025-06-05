class Employee:
    def __init__(self,salary,department,name):
        self.__salary = salary
        self._department = department
        self.Name = name

    def display(self):
        print("Department name is : ",self._department)
        print("Salary of the employee is : ",self.__salary)

def main():
    print("Enter name of employee : ")
    name = input()
    print("Enter the department name : ")
    department = input()
    print("Enter the salary :" )
    salary = int(input())

    obj = Employee(salary,department,name)
    print("Name of the employee is : ",obj.Name)

    obj.display()

if __name__ == "__main__":
    main()