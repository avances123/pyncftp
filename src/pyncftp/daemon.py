'''
Created on 12/02/2012

@author: fabio
'''
from tasks import *

creaTarea.delay()
for i in range(1,10):
    enviaFTP.delay()
