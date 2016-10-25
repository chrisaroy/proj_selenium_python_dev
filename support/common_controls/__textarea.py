# Class for Text areas
from selenium.webdriver.common.keys import Keys
from support.common_controls.__textbox import TextBox
import support.config as config
import logging
import time


class TextArea(TextBox):
    """Common class for text area elements/widgets"""
    def select_return(self, wait=True, wait_time=config.wait_time):
        """
        Selects the return key.
        :param wait: True - Wait before performing action
                     False - Do not wait before performing action
        :param wait_time: Time to wait before performing action.
        :return:
        """
        logging.info('Select the return key in ' + self.name)
        textbox = self.x_driver.find_element(self.x_elem_id[0], self.x_elem_id[1])
        if wait:
            time.sleep(wait_time)
        textbox.send_keys(Keys.RETURN)
