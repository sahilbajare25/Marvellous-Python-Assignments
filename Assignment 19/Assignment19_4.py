import sys
import CheckList
import os
import shutil

def DirectoryCopy(DirName1,DirName2,Extension):

    DirName1 = CheckList.checkPath(DirName1)

    CheckList.checkIfExist(DirName1)

    CheckList.checkIfDirectory(DirName1)

    try:
        os.mkdir(DirName2)
    except FileExistsError:
        print("Directory aleady exists")

    for folder, subfolder, files in os.walk(DirName1):
        
        for file in files:
            first_file = os.path.join(folder,file)
            second_file = os.path.join(DirName2,file)
            if file.endswith(Extension):
                shutil.copy(first_file,second_file)

def main():

    DirectoryCopy(sys.argv[1],sys.argv[2],sys.argv[3])

if __name__ == "__main__":
    main()