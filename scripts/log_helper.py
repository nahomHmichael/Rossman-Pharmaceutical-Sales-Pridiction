from asyncio.log import logger
import logging

#logger = logging.getLogger(__name__)
#logger.setLevel(logging.DEBUG)
#file_handler = logging.FileHandler('../logs/data_cleaning.log')
#formatter = logging.Formatter("time: %(asctime)s, function: %(funcName)s, module: %(name)s, message: %(message)s \n")

#file_handler.setFormatter(formatter)
#file_handler.setLevel(logging.INFO)
#logger.addHandler(file_handler)

class Logger_class: 
    def __init__(self,name,level=logging.INFO) :
        logger = logging.getLogger(__name__)
        logger.setLevel(level)
        file_handler = logging.FileHandler(name)
        formatter = logging.Formatter("time: %(asctime)s, \
                                      function: %(funcName)s, module: %(name)s, message: %(message)s \n")
        file_handler.setFormatter(formatter)
        logger.addHandler(name)
        self.logger = logger
    def get_logger(self):
        return self.logger
    
        