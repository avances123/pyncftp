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
        time.sleep(10)
    else:
        time.sleep(2)
    print current_process().name,t
   
if __name__ == '__main__':
    configdb = config.ConfigDB()
    rules = configdb.rules
        
    x = queue.TransferQueue()
    task_list = x.transfer_list
    
    q = Queue()
    
    workers = [ Process(target=worker, args=(q,)) for i in range(NUMWORKERS) ]
    
    for each in workers:
        each.start()
    for i in task_list:
        q.put(i)
    for each in workers:
        each.join()       
        

        
