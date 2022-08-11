import time
import threading

def doSleep(number):
    co = 0.2
    time.sleep(co*1.1**number)
    print(number)

arr = [-5,2,3,1,4]
thread_list = []
n = len(arr)

for i in range(n):
    t = threading.Thread(target=doSleep, args=[arr[i]])
    thread_list.append(t)

for t in thread_list:
    t.start()

for t in thread_list:
    t.join()