import schedule
import time

def display():

    print("Do coding...")

def main():

    schedule.every(30).minutes.do(display)

    while(True):
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()