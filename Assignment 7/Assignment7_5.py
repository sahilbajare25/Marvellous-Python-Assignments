# check palindrome string

def main():
    print("Enter a string : ")
    String = input()

    lenght = len(String)
    counter = 0

    for i in range(lenght):
        if String[i] == String[(lenght -1)-i]:
            counter = counter + 1
    
    if counter == lenght:
        print(String," is a palindrome")
    else:
        print(String," is not a palindrome")

if __name__ == "__main__":
    main()