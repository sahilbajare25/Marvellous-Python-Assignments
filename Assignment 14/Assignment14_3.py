class Book:
    def __init__(self,A):
        self.__price = A

    def set(self,value):
        self.__price = self.__price + value

    def get(self):
        print("The value of book is : ",self.__price)

def main():

    obj = Book(1000)
    obj.set(1500)
    obj.get()


if __name__ == "__main__":
    main()