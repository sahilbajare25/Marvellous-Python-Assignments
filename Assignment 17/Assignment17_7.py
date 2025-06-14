import schedule
import time
import sys

def FileActions():

    t = time.strftime("%M")

    print("Inside function")

    FileName = "Demo2backup%s.log" %(t)

    fb1 = open("Demo2.txt","r")

    fb2 = open(FileName,"w")

    for line in fb1:
        fb2.write(line)

    fb = open("backup_log.txt","a")

    timestamp = time.ctime()

    border = "*"*42
    fb.write("\n"+border+"\n")
    fb.write(timestamp)
    fb.write("\n"+border+"\n")

    fb1.close()
    fb2.close()


def main():

    schedule.every(30).minutes.do(FileActions)

    while(True):
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()