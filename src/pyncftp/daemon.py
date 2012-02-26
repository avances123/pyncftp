'''
Created on 12/02/2012

@author: fabio
'''

from db import config, queue
from net import ftp
from multiprocessing import Queue,Process ,current_process,log_to_stderr

import logging
import random
import time
    
logger = log_to_stderr()
logger.setLevel(logging.INFO)
NUMWORKERS = 4


def worker(tasks):
    
    t = tasks.get()
    if t[0] == 1:
        time.sleep(1)
    else:
        time.sleep(2)
    print current_process().name,t
   
if __name__ == '__main__':
    rules = config.ConfigDB().rules
    #rules = configdb.rules
    
    x = queue.TransferQueue()
    x.fillRandomQueue(10)
    q = Queue()
    for i in x.refreshQueue():
        q.put(i)
    logger.error("Tamanio: %s" % q.qsize())     
    while True:
        while not q.empty():
            workers = [ Process(target=worker, args=(q,)) for i in range(NUMWORKERS) ]
            for each in workers:
                each.start()
            for each in workers:
                each.join(5)                       
            
        logger.error("Tamanio lista %s" % len(x.refreshQueue()))
        time.sleep(2)
        
        for i in x.refreshQueue():
            q.put(i)
        logger.error("Tamanio Cola: %s" % q.qsize())
        
