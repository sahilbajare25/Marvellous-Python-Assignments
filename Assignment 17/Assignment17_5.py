import schedule
import time
import sys

def writeTime(FileName = "Marvellous.txt"):

    fb = open(FileName,"a")

    fb.write(time.ctime())

    fb.close()

def main():

    schedule.every(5).minutes.do(writeTime)

    while(True):
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()