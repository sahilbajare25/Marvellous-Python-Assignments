num = 1

def display(val):
    global num
    if val>=1:
        print(num)
        num = num + 1
        val = val - 1
        display(val)

def main():
    print("Enter a number : ")
    no = int(input())

    display(no)

if __name__ == "__main__":
    main()