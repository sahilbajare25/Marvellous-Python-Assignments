import sys

def enterNumbers(FileName):

    fb = open(FileName,"w")

    for i in range(2,12):
        data = sys.argv[i]
        fb.write(data+"\n")

    fb.close()

def main():
    
    enterNumbers(sys.argv[1])

if __name__ == "__main__":
    main()