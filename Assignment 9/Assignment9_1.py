import threading
import time

def display(delay):
    time.sleep(delay)
    for i in range(1,6):
        print(i)

def main():

    #start_timeT1 = time.time()
    T1 = threading.Thread(target=display,args=(1,))
    #end_timeT1 = time.time()
    T1.start()
    T1.join()

    #start_timeT2 = time.time()
    T2 = threading.Thread(target=display,args=(1,))
    #end_timeT2 = time.time()
    T2.start()
    T2.join()

    #start_timeT3 = time.time()
    T3 = threading.Thread(target=display,args=(1,))
    #end_timeT3 = time.time()
    T3.start()
    T3.join()

if __name__ == "__main__":
    main()