import sys

def writeName(FileName):

    fb = open(FileName,"w")

    for i in range(2,7):
        data = sys.argv[i]
        fb.write(data+"\n")
        print()

    fb.close()

def main():

    writeName(sys.argv[1])

if __name__ == "__main__":
    main()