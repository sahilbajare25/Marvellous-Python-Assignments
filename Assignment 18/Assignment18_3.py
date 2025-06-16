import sys

def copy(FileName1,FileName2):

    fb1 = open(FileName1,"r")
    fb2 = open(FileName2,"w")

    for line in fb1:
        fb2.write(line)

    fb1.close()
    fb2.close()

def main():

    copy(sys.argv[1],sys.argv[2])

if __name__ == "__main__":
    main()