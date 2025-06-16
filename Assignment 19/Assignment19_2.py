import sys
import os
import CheckList

def DirectoryRename(DirName,ext1,ext2):

    DirName = CheckList.checkPath(DirName)

    CheckList.checkIfExist(DirName)

    CheckList.checkIfDirectory(DirName)
    
    for folder, subfolder, files in os.walk(DirName):

        for file in files:
            if file.endswith(ext1):
                first,last = os.path.splitext(file)
                new_file = first + ext2
                os.rename(os.path.join(folder,file),new_file)

def main():

    DirectoryRename(sys.argv[1],sys.argv[2],sys.argv[3])

if __name__ == "__main__":
    main()