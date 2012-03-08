import random
import time
from celery.task import task
from random import choice
import ftplib
import json

@task(default_retry_delay=6,max_retries=2)
def enviaFTP(): # Segundos
    try:
    	resultados = [0,1,2,3,4,5,6]
    	tiempo = random.random()*10
    	logger = enviaFTP.get_logger()
    	logger.warning("Haciendo una subida de FTP que dura %s segundos" % tiempo)
    	time.sleep(tiempo)
    	#return choice(resultados)
	if tiempo >= 2:
	    raise ftplib.error_perm
	    #raise Exception

    except Exception,exc:
	logger.warning("Reintentando")
	enviaFTP.retry(exc=exc)
	#logger.error(e)


@task
def creaTarea():
    s="abcdef123"
    datos = {}
    datos['host'] = ''.join(random.sample(s,len(s)))
    datos['user'] = ''.join(random.sample(s,len(s)))
    datos['pass'] = ''.join(random.sample(s,len(s)))
    datos['file'] = ''.join(random.sample(s,len(s)))
    datos['remote-dir'] = ''.join(random.sample(s,len(s)))
    f = open('tarea.txt',"w")
    json.dump(datos,f)
    logger = creaTarea.get_logger()
    logger.info("Creando tarea")
    f.close()

