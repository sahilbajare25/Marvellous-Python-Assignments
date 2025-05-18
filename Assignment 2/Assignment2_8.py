def main():
    print("Enter a number :")
    No = int(input())
    counter = 1

    for i in range(1,No+1):
        for j in range(1,No+1):
                
                if j > counter:
                     break
                
                print(j,end=" ")
        
        counter = counter + 1
        print()

if __name__ == "__main__":
    main()