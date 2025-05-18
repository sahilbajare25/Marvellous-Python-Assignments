def main():
    print("Enter a number :")
    No = int(input())
    ans = 1

    for i in range(No+1):
        if i == 0:
            continue
        ans = ans * i
    
    print("Factorial of number : ",No," is : ",ans)


if __name__ == "__main__":
    main()