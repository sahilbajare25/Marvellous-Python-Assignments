import sys
import os
import time
import psutil

def procInfoLog():

    listofProcess = []

    for proc in psutil.process_iter():
        Dict1 = proc.as_dict(attrs=['name','pid','username'])
        listofProcess.append(Dict1)

    return listofProcess

def createDirectory(Dirname):

    if not os.path.exists(Dirname):
        os.mkdir(Dirname)

    timestamp = time.strftime('%H')

    Filename = "Marvellous%s.log" %(timestamp)

    Filename = os.path.join(Dirname,Filename)

    fobj = open(Filename,"w")

    data = procInfoLog()

    for value in data:
        fobj.write("%s \n\n" %(value))

    fobj.close()

def main():

    createDirectory(sys.argv[1])

if __name__ == "__main__":
    main()