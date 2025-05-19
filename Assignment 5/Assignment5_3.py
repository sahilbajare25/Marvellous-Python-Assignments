# Voting eligibility checker

def main():
    print("Enter age : ")
    Age = int(input())

    if Age >= 18:
        print("Eligible for vote")
    else:
        print("Age should be 18 or above to vote") 

if __name__ == "__main__":
    main()