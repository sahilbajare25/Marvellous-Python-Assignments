num = 1
def display(val):
    global num
    if num > val:
        return
    else:
        print(" * "*num)
        num = num + 1
        display(val)

def main():
    print("Enter a number : ",end="")
    no = int(input())

    display(no)
    

if __name__ == "__main__":
    main()