class Student:
    School_name = ""

    def __init__(self,A,B):
        self.Name = A
        self.RollNo = B

    def displayInfo(self):
        print("Student Details :")
        print("Name : ",self.Name)
        print("Roll Number : ",self.RollNo)

    @classmethod
    def displayDetails(cls):
        print("Name of the school is : ",cls.School_name)


def main():

    print("Enter the name of Student : ")
    Name = input()
    print("Enter the Roll number : ")
    RollNo = int(input())

    obj = Student(Name,RollNo)

    obj.displayInfo()

    Student.School_name = "Sinhagad"

    Student.displayDetails()


if __name__ == "__main__":
    main()