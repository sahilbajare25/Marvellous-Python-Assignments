def main():
    print("Enter a number :")
    No = int(input())
    val = No

    for i in range(No):
        for j in range(val):
            print(" * ",end=" ")
        
        val = val - 1
        print()

if __name__ == "__main__":
    main()