import sys

def main():

    FileName = sys.argv[1]

    fb = open(FileName,"r")
    print("Content of file is : ",fb.read())

    fb.close()

if __name__ == "__main__":
    main()