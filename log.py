import os
import logging
from datetime import datetime

class Log:

    def __init__(self, path, filename):
        self.path = self.create_dir(path)
        self.logger = self.start_logger(self.path, filename)

    def create_dir(self, path):
        if not os.path.exists(path):
            os.makedirs(path)
        return path

    def start_logger(self, path, filename):
        log_formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s')
        root_logger = logging.getLogger()
        root_logger.setLevel(logging.DEBUG)
        file_handler = logging.FileHandler("{}\\{}-{}.log".format(path, filename, datetime.now().strftime('%Y_%m_%d')))
        file_handler.setFormatter(log_formatter)
        root_logger.addHandler(file_handler)

        console_handler = logging.StreamHandler()
        console_handler.setFormatter(log_formatter)
        root_logger.addHandler(console_handler)
        return root_logger

    def clear_handlers(self):
        # Clear log handlers
        handlers = self.logger.handlers[:]
        for handler in handlers:
            handler.close()
            self.logger.removeHandler(handler)