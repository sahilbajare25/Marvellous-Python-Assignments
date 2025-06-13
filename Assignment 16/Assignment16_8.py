import sys

def check(FileName1,FileName2):

    fb1 = open(FileName1,"r")

    fb2 = open(FileName2,"w")

    for line in fb1:
        if not line.isspace():
            fb2.write(line)

    fb1.close()
    fb2.close()

def main():

    check(sys.argv[1],sys.argv[2])

if __name__ == "__main__":
    main()