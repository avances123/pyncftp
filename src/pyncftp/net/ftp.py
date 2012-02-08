'''
Created on 08/02/2012

@author: Fabio Rueda <avances123@gmail.com>
'''

import ftplib

class Ftp(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        filename = 'test.txt'
        f = open(filename,"rb")
        conn = ftplib.FTP('avances123.dyndns.org')
        conn.debug(1)  # See server messages
        conn.set_pasv(False) # Control pasv connections
        conn.login('fabio', 'fabiete123')
        conn.storbinary('STOR ' + filename, f)  # basename and filehandler
        f.close()
        conn.quit()

if __name__ == '__main__':
    print 'Hello World'
    a = Ftp()  
    