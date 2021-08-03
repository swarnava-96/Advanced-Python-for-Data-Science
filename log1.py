import logging
logging.basicConfig(filename ="log1.txt",
                    filemode= 'a',
                    format= '%(asctime)s %(levelname)s-%(message)s',
                    datefmt= '%Y-%m-%d %H:%M:%S')

# Using try except

i = 10
try:
    i = i/0
except:
    logging.error("Division by 0 Error")

