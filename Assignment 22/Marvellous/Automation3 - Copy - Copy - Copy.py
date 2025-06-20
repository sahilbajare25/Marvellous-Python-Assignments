import schedule
import time
import datetime


def MySchedule():
    print("Inside MySchedule function at :",datetime.datetime.now())

def main():
    print("Inside Automation Script")
    print("Current time is :",datetime.datetime.now())

    schedule.every(20).seconds.do(MySchedule)

    print("Application is in waiting state :")

    time.sleep(50)
    
if __name__ == "__main__":
    main()