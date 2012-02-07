'''
Created on 08/02/2012

@author: Fabio Rueda <avances123@gmail.com>
'''

# easy_install pysftp
import pysftp


class Sftp(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        srv = pysftp.Connection(host, username, private_key, password, port, private_key_pass, log)


if __name__ == '__main__':
    print 'Hello World'
    a = Sftp()  
    