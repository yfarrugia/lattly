__author__ = 'yanikafarrugia'

import logging

# create logger with 'lattly'
logger = logging.getLogger('lattly')
logger.setLevel(logging.DEBUG)

# create file handler which logs even debug messages
file_handler = logging.FileHandler('lattly.log')
file_handler.setLevel(logging.DEBUG)

# create console handler with a higher log level
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.ERROR)

# create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# add the handlers to the logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)
