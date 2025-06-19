import psutil

def ProcInfo():

    for proc in psutil.process_iter():
        info = proc.as_dict(attrs=["pid","name","username"])
        print(info)

def main():

    ProcInfo()

if __name__ == "__main__":
    main()