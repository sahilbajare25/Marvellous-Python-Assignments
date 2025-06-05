class Vehicle:

    def Start(self):
        print("Inside Base class Vehicle")

class Car(Vehicle):

    def Start(self):
        print("Inside Child class Car")

def main():

    obj = Car()
    obj.Start()

if __name__ == "__main__":
    main()