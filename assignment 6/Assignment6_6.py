#Triangle pattern 

def main():
    num = 0
    for i in range(4):
        for j in range(4):
            if j <= num:
                print(" * ", end=" ")
            
        print()
        num = num + 1

if __name__ == "__main__":
    main()