# Class for <element_type>
from support.common_controls.__base_element import BaseElement
import support.config as config
import logging
import time


class Template(BaseElement):
    """Common class for <element_type> elements/widgets"""
    def action(self, wait=True, wait_time=config.wait_time):
        """
        Description
        :param:
        :param wait: True - Wait before performing action
                     False - Do not wait before performing action
        :param wait_time: Time to wait before performing action.
        :return: None
        """
        logging.info('<action to>' + self.name)
        button = self.x_driver.find_element(self.x_elem_id[0], self.x_elem_id[1])
        if wait:
            time.sleep(wait_time)
        button.click()

# Note: Once code is complete, add import statement to common_controls/__init__.py
