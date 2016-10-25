# Module for creating test logs
import logging
import support.config


class TestLog(object):
    def __init__(self, debug_level=logging.INFO):
        self.debug_level = debug_level

        # Setting up logging to text file
        test_log = support.config.test_log_folder + '_' + support.config.test_name + '.log'
        logging.basicConfig(filename=test_log, filemode='w',
                            format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p - ',
                            level=self.debug_level)

        # Setting up logging to console
        std_err_logger = logging.StreamHandler()
        std_err_logger.setFormatter(logging.Formatter(logging.BASIC_FORMAT))
        logging.getLogger().addHandler(std_err_logger)
