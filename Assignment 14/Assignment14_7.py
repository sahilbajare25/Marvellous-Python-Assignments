class Person:
    def __init__(self,name,age):
        self.Name = name
        self.Age = age
        print("Name : ",self.Name)
        print("Age : ",self.Age)

class Teacher(Person):
    def __init__(self,name,age,subject,salary):
        super().__init__(name,age)
        self.Subject = subject
        self.Salary = salary
        print("Subject : ",self.Subject)
        print("Salary : ",self.Salary)

def main():
    print("Enter the Name :")
    Name = input()
    print("Enter the age : ")
    Age = int(input())
    print("Enter the subject : ")
    Subject = input()
    print("Enter the salary :")
    salary = int(input())

    obj = Teacher(Name,Age,Subject,salary)

if __name__ == "__main__":
    main()