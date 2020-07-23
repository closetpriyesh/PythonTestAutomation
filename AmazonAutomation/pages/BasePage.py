import inspect
import logging


class BasePage:

    def __init__(self):
        stack = inspect.stack()[1][1].split("\\")
        stack_length = len(stack)
        logger_name = stack[stack_length - 2] + "\\" + stack[stack_length - 1]
        # logger = logging.getLogger(__name__)
        self.logger = logging.getLogger(logger_name)
        file_handler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s: %(message)s")
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)  # file_handler object
        self.logger.setLevel(logging.INFO)
