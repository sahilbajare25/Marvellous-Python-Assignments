import sys
import CheckList
import os
import shutil

def DirectoryCopy(DirName1,DirName2):

    DirName1 = CheckList.checkPath(DirName1)

    CheckList.checkIfExist(DirName1)

    CheckList.checkIfDirectory(DirName1)

    try:
        shutil.copytree(DirName1,DirName2)
    except FileExistsError:
        print("Directory already Exist")
    finally:
        print("All data copied succesfully to new directory")
    

def main():

    DirectoryCopy(sys.argv[1],sys.argv[2])

if __name__ == "__main__":
    main()