'''
Created on 12/02/2012

@author: fabio
'''
import psycopg2
from psycopg2 import extras
import Queue
import json

# Make heritance from Queue class 
class TransferQueue(object):
    '''
    classdocs
    '''
    def refreshQueue(self,oldqueue=None):
        conn = psycopg2.connect("dbname=pyncftp user=fabio")
        #cur = conn.cursor()
        cur = conn.cursor()
        cur.execute("SELECT * FROM queue;")
        rowlist = cur.fetchall()
        transfer_queue = Queue.Queue(0)
        for row in rowlist:
            transfer_queue.put(row)
        conn.commit()
        cur.close()
        conn.close()
        return transfer_queue

    def __init__(self):
        '''
        Constructor
        '''
        self.transfer_queue = self.refreshQueue()
        print self.transfer_queue
        #print json.dumps(self.transfer_queue, sort_keys=True, indent=4)
        
        
if __name__ == '__main__':
    a = TransferQueue()
