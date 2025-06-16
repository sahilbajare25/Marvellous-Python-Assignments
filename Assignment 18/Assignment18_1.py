import sys
import os

def check(Filename):

    ret = os.path.exists(Filename)

    if ret == True:
        print("File Exists")
    else:
        print("File not Exists")

def main():

    check(sys.argv[1])

if __name__ == "__main__":
    main()