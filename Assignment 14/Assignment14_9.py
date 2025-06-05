class Product:
    def __init__(self,name,price):
        self.Name = name
        self.Price = price

    def __eq__(self, value):
        if isinstance(value,Product):
            return self.Name == value.Name and self.Price == value.Price
        else:
            return False

def main():
    print("Enter name of product :")
    product1 = input()
    print("Enter price of product : ")
    price1 = int(input())

    print("Enter name of product :")
    product2 = input()
    print("Enter price of product : ")
    price2 = int(input())

    print("Enter name of product :")
    product3 = input()
    print("Enter price of product : ")
    price3 = int(input())

    obj1 = Product(product1,price1)
    obj2 = Product(product2,price2)
    obj3 = Product(product3,price3)

    print(obj1 == obj2)
    print(obj2 == obj3)

if __name__ == "__main__":
    main()