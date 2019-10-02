# 生产者消费者模型
from threading import Thread, current_thread
import time
import random
from queue import Queue

queue = Queue(5)


class ProducerThread(Thread):
    def run(self):
        name = current_thread().getName()
        totalNum = range(100)
        global queue
        while True:
            num = random.choice(totalNum)
            queue.put(num)
            print('生产者%s生产了数据%s' % (name, num))
            t = random.randint(1, 3)
            time.sleep(t)
            print('生产者%s休眠了%s秒' % (name, t))


class ConsumerThread(Thread):
    def run(self):
        name = current_thread().getName()
        global queue
        while True:
            num = queue.get()
            queue.task_done()
            print('消费者%s消耗了数据%s' % (name, num))
            t = random.randint(1, 5)
            time.sleep(t)
            print('消费者%s休眠了%s秒' % (name, t))


producer1 = ProducerThread(name='producer1')
producer1.start()

consumer1 = ConsumerThread(name='consumer1')
consumer1.start()
