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
        conn = ftplib.FTP('localhost')
        conn.debug(1)  # See server messages
        conn.set_pasv(False) # Control pasv connections
        conn.login('farios', 'farios')
        return conn
 
    def kill_conn(self  ):
        self.conn.quit()
    
    def rename_file(self):
        pass
    
    def delete_file(self):
        pass   
    
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
    