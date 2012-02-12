'''
Created on 08/02/2012

@author: Fabio Rueda <avances123@gmail.com>
'''

import ftplib

class FtpTransfer(object):
    '''
    classdocs
    '''

    def start_conn(self):
        conn = ftplib.FTP('avances123.dyndns.org')
        conn.debug(1)  # See server messages
        conn.set_pasv(False) # Control pasv connections
        conn.login('fabio', 'fabiete123')
        return conn
 
    def kill_conn(self  ):
        self.conn.quit()
    
    def upload_file(self, filename):
        f = open(filename,"rb")
        self.conn.storbinary('STOR ' + filename, f)  # basename and filehandler
        f.close()

    

    def __init__(self):
        '''
        Constructor
        '''
        self.conn = self.start_conn()  
        

if __name__ == '__main__':
    print 'Subiendo un fichero'
    a = FtpTransfer()  
    a.upload_file('test.txt')
    # Some other operations 
    a.kill_conn()
    