#largest number among 5 numbers

def main():
    print("Enter five numbers : ")
    Demo = list()

    for i in range(5):
        no = int(input())
        Demo.append(no)

    res = Demo[0]

    for i in Demo:
            if i > res:
                res = i
        
    print("Maximum number is : ",res)
    
if __name__ == "__main__":
    main()