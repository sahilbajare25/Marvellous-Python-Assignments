# calculate square and cube of number using lambda function

square = lambda x : x*x
cube = lambda x : x*x*x

def main():
    print("Enter a number :")
    no = int(input())

    ret = square(no)
    res = cube(no)

    print("Square : ",ret)
    print("Cube : ", res)

if __name__ == "__main__":
    main()