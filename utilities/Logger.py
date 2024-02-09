import logging
import inspect


class LoggenClass:
    @staticmethod
    def log_generator():
        log_name = inspect.stack()[1][3]
        logger = logging.getLogger(log_name)
        logfile = logging.FileHandler("D:\\Credence\\Tushar Sir\\selenium Part  2\\Project_tusharsir\\Pytest_Nopcommerce\\Logs\\NopCom_logs.log")
        log_format = logging.Formatter(
            " %(asctime)s : %(levelname)s : %(name)s : %(funcName)s : %(lineno)s : %(message)s ")
        logfile.setFormatter(log_format)
        logger.addHandler(logfile)
        logger.setLevel(logging.INFO)
        return logger
