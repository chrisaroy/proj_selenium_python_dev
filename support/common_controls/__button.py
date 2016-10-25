# Class for Buttons
from support.common_controls.__base_element import BaseElement
import support.config as config
import logging
import time


class Button(BaseElement):
    """Common class for button elements/widgets"""
    def click(self, wait=True, wait_time=config.wait_time):
        """
        Select/click on button
        :param wait: True - Wait before performing action
                     False - Do not wait before performing action
        :param wait_time: Time to wait before performing action.
        :return: None
        """
        logging.info('Select/click: ' + self.name)
        button = self.x_driver.find_element(self.x_elem_id[0], self.x_elem_id[1])
        if wait:
            time.sleep(wait_time)
        button.click()

    def get_text(self, wait=True, wait_time=config.wait_time):
        """
        Get text displayed on button
        :param wait: True - Wait before performing action
                     False - Do not wait before performing action
        :param wait_time: Time to wait before performing action.
        :return: text - Text displayed on button
        """
        logging.info('Get text from ' + self.name)

        button = self.x_driver.find_element(self.x_elem_id[0], self.x_elem_id[1])
        if wait:
            time.sleep(wait_time)
        text = button.text
        logging.info('Text from ' + self.name + ' is: ' + text)
        return text
