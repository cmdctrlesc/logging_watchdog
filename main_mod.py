import logging

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler("my_log.log")
logger.addHandler(file_handler)
logger.setLevel(logging.INFO)
stream_handler = logging.StreamHandler()
logger.addHandler(stream_handler)

print("main program is running")
logger.debug('DEBUG')
logger.info('INFO')