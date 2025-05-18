def main():
    print("Enter a number :")
    No = int(input())

    for i in range(No):
        for j in range(No):
            print(" * ",end=" ")
        
        print()

if __name__ == "__main__":
    main()