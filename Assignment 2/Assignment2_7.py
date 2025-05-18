def main():
    print("Enter a number :")
    No = int(input())

    for i in range(1,No+1):
        for j in range(1,No+1):
            print(j,end=" ")
        
        print()

if __name__ == "__main__":
    main()