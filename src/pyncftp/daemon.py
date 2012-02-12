'''
Created on 12/02/2012

@author: fabio
'''

from db import config, queue
from net import ftp
from multiprocessing import Pool


def f(x):
    print x   
   
if __name__ == '__main__':
    configdb = config.ConfigDB()
    rules = configdb.rules
    
    x = queue.TransferQueue()
    task_queue = x.transfer_queue
    print task_queue.get()
    #pool = Pool(processes=4)              # start 4 worker processes
    #result = pool.apply_async(f, [task_queue])    # evaluate "f(10)" asynchronously
    #print result.get()           # prints "100" unless your computer is *very* slow
    #print pool.map(f, range(10))          # prints "[0, 1, 4,..., 81]"
