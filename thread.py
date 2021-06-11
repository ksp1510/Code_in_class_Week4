#! /usr/local/bin/python3

import threading
import time


class MyThread(threading.Thread):  # subclass the Thread object
      def __init__(self, myId, count, mutex):
            self.myId = myId
            self.count = count  # per thread state information
            self.mutex = mutex  # shared objects, not globals
            threading.Thread.__init__(self)

      def run(self):  # run provides thread logic
            starttime = time.time()
            stoptime = starttime + 5
            print(starttime)
            with self.mutex:
                  while time.time() < stoptime:
                        # time.sleep(0.01)    # when this thread goes to sleep,
                        #  it will yield control of the mutex to
                        # another thread that is ready to run
                        for i in range(self.count):  # sync stdout access
                              print('[%s] => %s' % (self.myId, i))


stdoutmutex = threading.Lock()
threads = []
for i in range(10):
      thread = MyThread(i, 100, stdoutmutex)  # make/start 10 threads
      # thread.start()                          # starts run method in a thread
      threads.append(thread)

delay = 3.0
for thread in threads:
      print(thread.myId)
      timer = threading.Timer(delay, thread.start())
      # timer.start()
      delay += 3.0

time.sleep(60)
# for thread in threads:                      # wait for thread exits
#    thread.join()
print("Main thread exiting.")
