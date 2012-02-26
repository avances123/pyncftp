'''
Created on 12/02/2012

@author: fabio
'''
import psycopg2
import random

# Make heritance from Queue class 
class TransferQueue(object):
    '''
    classdocs
    '''
    def fillRandomQueue(self,num):
        
        conn = psycopg2.connect("dbname=pyncftp user=fabio")
        cur = conn.cursor()
        for i in range(num):
            cur.execute("INSERT INTO queue (localfile, type) VALUES (%s, %s)",    (random.random(), "abc'def"))
        conn.commit()
        cur.close()
        conn.close()
    
    
    
    def refreshQueue(self,oldqueue=None):
        conn = psycopg2.connect("dbname=pyncftp user=fabio")
        #cur = conn.cursor()
        cur = conn.cursor()
        cur.execute("SELECT * FROM queue;")
        rowlist = cur.fetchall()
        cur.close()
        conn.close()
        return rowlist

    def __init__(self):
        '''
        Constructor
        '''
        pass
        #self.fillRandomQueue(40)
        #self.transfer_list = self.refreshQueue()
        #print self.transfer_queue
        #print json.dumps(self.transfer_queue, sort_keys=True, indent=4)
        
        
if __name__ == '__main__':
    a = TransferQueue()
