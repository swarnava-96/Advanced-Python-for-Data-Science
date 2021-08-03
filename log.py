import logging
logging.basicConfig(filename = "Swarnava.txt",
                    filemode= 'a',
                    format= '%(asctime)s %(levelname)s-%(message)s',
                    datefmt= '%Y-%m-%d %H:%M:%S')
for i in range(0, 15):
    if(i%2 == 0):
        logging.warning('Log Warning Message')
    elif(i%3 == 0):
        logging.critical('Log Critical Message')
    else:
        logging.error('Log Error Message')
