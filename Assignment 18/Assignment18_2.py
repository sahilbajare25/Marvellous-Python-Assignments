import sys

def display(FileName):

    fb = open(FileName,"r")

    print("The contents of file are \n",fb.read())

def main():

    display(sys.argv[1])

if __name__ == "__main__":
    main()