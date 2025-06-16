import sys
import hashlib
import CheckList
import os

def DirectoryCheckSum(path, blocksize = 1024):

    fobj = open(path, "rb")

    hobj = hashlib.md5()

    buffer = fobj.read(blocksize)

    while(len(buffer) > 0):

        hobj.update(buffer)
        buffer = fobj.read(blocksize)

    fobj.close()

    return hobj.hexdigest()

def checkDirectory(FileName):

    FileName = CheckList.checkPath(FileName)

    CheckList.checkIfExist(FileName)

    CheckList.checkIfDirectory(FileName)

    for folders, subfolders , files in os.walk(FileName):

        for file in files:
            checksum = DirectoryCheckSum(os.path.join(folders,file))
            print("Checksum of ",file," is :",checksum)
            print()

def main():

    checkDirectory(sys.argv[1])

if __name__ == "__main__":
    main()