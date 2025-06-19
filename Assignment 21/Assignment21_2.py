import psutil
import sys

def ProcInfo(ProcessName):

    for proc in psutil.process_iter():
        Dict1 = proc.as_dict(attrs=["pid","name"])
        if(ProcessName in Dict1.values()):
            print(Dict1)
        
        

def main():

    ProcInfo(sys.argv[1])

if __name__ == "__main__":
    main()