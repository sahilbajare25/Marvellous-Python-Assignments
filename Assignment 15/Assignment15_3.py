import sys

def main():

    FileName1 = sys.argv[1]
    FileName2 = sys.argv[2]

    fd1 = open(FileName2,"w")

    fd2 = open(FileName1,"r")

    for line in fd2:
        fd1.write(line)

    fd1.close()
    fd2.close()

    fd3 = open(FileName2,"r")

    print(fd3.read())

    fd3.close()


if __name__ == "__main__":
    main()