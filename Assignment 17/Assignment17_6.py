import schedule
import time

def display():

    t = time.strftime("%H:%M")

    if t == "13:00":
        print("Lunch Time")
    elif t == "18:00":
        print("Wrap up work")


def main():

    schedule.every().day.at("13:00").do(display)
    schedule.every().day.at("18:00").do(display)

    while(True):
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()