import multiprocessing
import threading
import time

def summing(val):
    sum = 0
    for i in range(val+1):
          sum = sum + i

          

def main():
     number = 10000000
     start_timeF = time.time()
     summing(number)
     end_timeF = time.time()

     start_timeT = time.time()
     T1 = threading.Thread(target=summing,args=(number,))
     T1.start()
     end_timeT = time.time()

     start_timeP = time.time()
     P1 = multiprocessing.Process(target=summing,args=(number,))
     P1.start()
     end_timeP = time.time()

     print("Function : ",end_timeF-start_timeF," Thread : ",end_timeT-start_timeT," Process  : ",end_timeP-start_timeP)

if __name__ == "__main__":
    main()