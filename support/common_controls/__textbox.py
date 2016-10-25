# Class for Text boxes
from support.common_controls.__base_element import BaseElement
import support.config as config
import logging
import time


class TextBox(BaseElement):
    """Common class for Text box elements/widgets"""
    def clear_text(self, wait=True, wait_time=config.wait_time):
        """
        Clears any text within textbox or text area.
        :param wait: True - Wait before performing action
                     False - Do not wait before performing action
        :param wait_time: Time to wait before performing action.
        :return:
        """
        logging.info('Clear text in ' + self.name)
        textbox = self.x_driver.find_element(self.x_elem_id[0], self.x_elem_id[1])
        if wait:
            time.sleep(wait_time)
        textbox.clear()

    def enter_text(self, text, clear_text=True, wait=True, wait_time=config.wait_time):
        """
        Enter text into textbox.
        :param text: Text to enter into textbox
        :param clear_text: Clears text in the textbox
        :param wait: True - Wait before performing action
                     False - Do not wait before performing action
        :param wait_time: Time to wait before performing action.
        :return: None
        """
        logging.info('Enter: ' + text + self.name)
        textbox = self.x_driver.find_element(self.x_elem_id[0], self.x_elem_id[1])
        if wait:
            time.sleep(wait_time)
        if clear_text:
            self.clear_text()
        textbox.send_keys(text)
        logging.info('Entered text: ' + text)

    def get_text(self, wait=True, wait_time=config.wait_time):
        """
        Get text from textbox
        :param wait: True - Wait before performing action
                     False - Do not wait before performing action
        :param wait_time: Time to wait before performing action.
        :return: text entered into textbox
        """
        logging.info('Get text from ' + self.name)
        textbox = self.x_driver.find_element(self.x_elem_id[0], self.x_elem_id[1])
        if wait:
            time.sleep(wait_time)
        text = textbox.get_attribute('value')
        logging.info('Text in ' + self.name + ' is: ' + text)
        return text
