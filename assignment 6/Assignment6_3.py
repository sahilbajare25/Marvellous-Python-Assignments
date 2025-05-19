# print multiplication table of number up to 10

def main():
    print("Enter a number : ")
    no = int(input())

    for i in range(1,11):
        print(no," x ",i," = ",i*no)

if __name__ == "__main__":
    main()