def main():
    print("Enter a number :")
    No = int(input())
    ans = 0

    for i in range(No):
        if i == 0:
            continue
        if No%i == 0:
            ans = ans + i
    
    print("Addition of factors of ",No," is : ",ans)

if __name__ == "__main__":
    main()