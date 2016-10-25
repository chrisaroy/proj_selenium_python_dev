# Class for Radio Buttons
from support.common_controls.__checkbox import CheckBox
import support.config as config
import logging
import time


class RadioButton(CheckBox):
    """Common class for radio button elements/widgets """
    def is_selected(self, wait=True, wait_time=config.wait_time):
        """
        Determine if radio button is selected
        :param wait: True - Wait before performing action
                     False - Do not wait before performing action
        :param wait_time: Time to wait before performing action.
        :return: True if selected
                 False if not selected
        """
        logging.info('Determine if the ' + self.name + ' is selected.')
        checkbox = self.x_driver.find_element(self.x_elem_id[0], self.x_elem_id[1])
        if wait:
            time.sleep(wait_time)
        checked = checkbox.is_selected()
        logging.info('Selected state of: ' + self.name + " is: " + str(checked))
        return checked
