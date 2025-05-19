#  Vowel or consonant check

def main():
    print("Enter a character :")
    ch = input()

    if (ch == 'A' or ch == 'a') or (ch == 'E' or ch == 'e') or (ch == 'I' or ch == 'i') or (ch == 'O' or ch == 'o') or (ch == 'U' or ch =='u'):
        print(ch," is a Vowel")
    else:
        print(ch," is a Constant") 

if __name__ == "__main__":
    main()