import logging
logging.basicConfig(filename='example.log', level=logging.CRITICAL)
logging.debug('This message should go to the log file')
logging.critical('Critical error')
