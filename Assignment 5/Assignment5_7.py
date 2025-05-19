#Area and perimeter of rectangle

def main():
    print("Enter lenght :")
    len = int(input())

    print("Enter width :")
    wid = int(input())

    area = len*wid

    perimeter = 2 * (len + wid)

    print("Area : ",area)
    print("Perimeter : ",perimeter)


if __name__ == "__main__":
    main()