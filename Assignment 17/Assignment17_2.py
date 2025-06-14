import schedule
import datetime
import time

def display():
    ctime = datetime.datetime.now()
    print(ctime)

def main():

    schedule.every(1).minutes.do(display)

    while(True):
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()