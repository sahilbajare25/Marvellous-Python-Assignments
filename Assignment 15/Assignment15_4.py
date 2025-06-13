import sys

def main():

    FileName1 = sys.argv[1]
    Filename2 = sys.argv[2]

    temp1 = []
    temp2 = []

    fd1 = open(FileName1, "r")
    fd2 = open(Filename2, "r")

    for line in fd1:
        temp1.append(line.strip("\n").split())

    for line in fd2:
        temp2.append(line.strip("\n").split())

    if (temp1 == temp2):
        print("Both are same")
    else:
        print("Both are different")

    fd1.close()
    fd2.close()        

if __name__ == "__main__":
    main()