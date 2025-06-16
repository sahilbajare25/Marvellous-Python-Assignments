import os

def checkPath(Name):

    Dpath = os.path.isabs(Name)

    if Dpath == False:
        Dpath = os.path.abspath(Name)

    return Dpath

def checkIfExist(Name):

    flag = os.path.exists(Name)

    if flag == False:
        print("Path is invalid")
        exit()
    else:
        print("Corrrect Path")

def checkIfDirectory(Name):
    
    flag = os.path.isdir(Name)

    if flag == False:
        print("Not a Directory")
        exit()
    else:
        print("Correct Directory")