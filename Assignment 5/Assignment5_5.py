#Even or odd number check

def main():
    print("Enter a number :")
    no = int(input())

    if no%2 == 0:
        print(no," is an even number")
    else:
        print(no," is an odd number")

if __name__ == "__main__":
    main()