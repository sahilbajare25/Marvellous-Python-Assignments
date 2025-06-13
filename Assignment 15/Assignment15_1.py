import os
import sys

def main():

    FileName = sys.argv[1]

    ret = os.path.exists(FileName)

    if ret == True:
        print("File is present")
    else:
        print("File is not present")

if __name__ == "__main__":
    main()