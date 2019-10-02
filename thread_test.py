import threading
import time
from threading import current_thread


def myThread(arg1, arg2):
    print(current_thread().getName(), 'start')
    print('%s %s' % (arg1, arg2), end='||')
    print('{0} {1}'.format(arg1, arg2))
    s = 'this is the first sentence.' \
        'this is the second sentence.'
    print(s)
    time.sleep(1)
    print(current_thread().getName(), 'stop')


for i in range(1, 10, 1):
    # thread1 = myThread(i,i+1)
    thread1 = threading.Thread(target=myThread, args=(i, i + 1))
    thread1.start()
    thread1.join()
