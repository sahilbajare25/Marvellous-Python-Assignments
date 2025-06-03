class Bookstore:
    NoOfBooks = 0
    def __init__(self,A,B):
        self.Name = A
        self.Author = B
        Bookstore.NoOfBooks = Bookstore.NoOfBooks + 1

    def Display(self):
        print("Name of Book is : ",self.Name)
        print("Author of Book is : ",self.Author)
        print("Number of Book are : ",Bookstore.NoOfBooks)

def main():

    print("Enter the name of the book : ")
    Name = input()
    print("Enter author name :")
    Author = input()

    obj = Bookstore(Name,Author)
    obj.Display()

    print("Enter the name of the book : ")
    Name = input()
    print("Enter author name :")
    Author = input()

    obj = Bookstore(Name,Author)
    obj.Display()

if __name__ == "__main__":
    main()