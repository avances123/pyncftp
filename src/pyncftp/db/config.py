'''
Created on 12/02/2012

@author: fabio
'''
import psycopg2
from psycopg2 import extras
import json

class ConfigDB(object):
    '''
    classdocs
    '''
    def importConfig(self):
        conn = psycopg2.connect("dbname=pyncftp user=fabio")
        #cur = conn.cursor()
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

        cur.execute("SELECT * FROM config;")
        config_list = cur.fetchall()
        conn.commit()
        cur.close()
        conn.close()
        return config_list

    def __init__(self):
        '''
        Constructor
        '''
        self.rules = self.importConfig()
        #print json.dumps(self.rules, sort_keys=True, indent=4)
        
        
if __name__ == '__main__':
    a = ConfigDB()
