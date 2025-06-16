import sys
import hashlib
import CheckList
import os
import time

def DirectoryCheckSum(path, blocksize = 1024):

    fobj = open(path, "rb")

    hobj = hashlib.md5()

    buffer = fobj.read(blocksize)

    while(len(buffer) > 0):

        hobj.update(buffer)
        buffer = fobj.read(blocksize)

    fobj.close()

    return hobj.hexdigest()

def displayAndDelete(MyDict,FileName):

    FileName = CheckList.checkPath(FileName)

    Flag = os.path.exists(FileName)

    if Flag == False:
        fobj = open(FileName,"w")
    else:
        fobj = open(FileName, "a")

    Result = list(filter(lambda x : len(x) >1, MyDict.values()))
    
    count = 0
    
    for value in Result:
        for subvalue in value:
            count = count + 1
            if count > 1:
                fobj.write("%s \n" %(subvalue))
                os.remove(subvalue)
        
        count = 0

    fobj.close()

def checkDirectory(FileName):

    FileName = CheckList.checkPath(FileName)

    CheckList.checkIfExist(FileName)

    CheckList.checkIfDirectory(FileName)

    Duplicate = {}

    for folders, subfolders , files in os.walk(FileName):

        for file in files:
            fname = os.path.join(folders,file)
            checksum = DirectoryCheckSum(fname)
            
            if checksum in Duplicate:
                Duplicate[checksum].append(fname)
            else:
                Duplicate[checksum] = [fname]
        
    return Duplicate

def main():

    Start_time = time.time()
    result = checkDirectory(sys.argv[1])
    displayAndDelete(result,sys.argv[2])
    End_time = time.time()
    print("Time required for the script is : ",(End_time-Start_time))

if __name__ == "__main__":
    main()