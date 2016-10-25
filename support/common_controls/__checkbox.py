# Class for Check Boxes
from support.common_controls.__base_element import BaseElement
import support.config as config
import logging
import time


class CheckBox(BaseElement):
    """Common class for checkbox elements/widgets"""
    def select(self, wait=True, wait_time=config.wait_time):
        """
        Select the checkbox
        :param wait: True - Wait before performing action
                     False - Do not wait before performing action
        :param wait_time: Time to wait before performing action.
        :return: None
        """
        logging.info('Select/click the ' + self.name)
        checkbox = self.x_driver.find_element(self.x_elem_id[0], self.x_elem_id[1])
        if wait:
            time.sleep(wait_time)
        checkbox.click()

    def is_checked(self, wait=True, wait_time=config.wait_time):
        """
        Determine if checkbox is checked
        :param wait: True - Wait before performing action
                     False - Do not wait before performing action
        :param wait_time: Time to wait before performing action.
        :return: True if checked
                 False if not checked
        """
        logging.info('Determine if the ' + self.name + ' is checked.')
        checkbox = self.x_driver.find_element(self.x_elem_id[0], self.x_elem_id[1])
        if wait:
            time.sleep(wait_time)
        checked = checkbox.is_selected()
        logging.info('Checked state of: ' + self.name + " is: " + str(checked))
        return checked
