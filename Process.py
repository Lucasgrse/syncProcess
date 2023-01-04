import signal

from multiprocessing import Semaphore
from threading import Thread
from time import sleep

control = Semaphore()
 
count = 0

run = True

def signal_handler(signal, trace):
  global running
  running = False

signal.signal(signal.SIGINT, signal_handler)

class Process(Thread):
    
    def __init__(self, p):
        Thread.__init__(self)
        self.p = p    
    
    def run(self):
        global count    
        while run:
            with control:
                print(" [sync] - Semaphore {0} acquired".format(self.p))
                
                count += 1
                
                print ("\n Process: {0}, entered the critical region, count: {1} \n".format(
                    self.p, count))                 
                sleep(5)                
                print(" [sync] - Semaphore {0} released ".format(self.p))                
                sleep(2)                                       
                print ("Process: {0}, left the critical region, count: {1} \n".format(self.p, count))
                
            sleep(3)
            
                             
p1 = Process(0)
p2 = Process(1)

p1.start()
p2.start()

p1.join()
p2.join()    