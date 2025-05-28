import multiprocessing

def square(values):
    print("Square values of the list are :")
    for i in values:
        print(i*i)


def main():
    print("Enter the length of list :")
    length = int(input())

    Demo = []

    print("Enter the elements : ")
    for i in range(length):
        val = int(input())
        Demo.append(val)

    p1 = multiprocessing.Process(target=square,args=(Demo,))
    p1.start()

if __name__ == "__main__":
    main()