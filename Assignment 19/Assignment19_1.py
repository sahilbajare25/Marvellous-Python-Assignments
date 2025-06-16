import sys
import os
import CheckList

def checkDirectory(Name,Extension):

    Name = CheckList.checkPath(Name)

    print("Absolute path is : ",Name)

    CheckList.checkIfExist(Name)

    CheckList.checkIfDirectory(Name)

    temp = []

    for folder, subfolder, files in os.walk(Name):
        
        for file in files:
            if file.endswith(Extension):
                #temp.append(os.path.join(folder,file))
                temp.append(file)

    print(temp)

def main():

    checkDirectory(sys.argv[1],sys.argv[2])

if __name__ == "__main__":
    main()