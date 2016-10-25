# Classes for alerts and pop-up windows
import support
import logging

"""
In order to use the alert, the following need to be imported where the button that brings up the alert appears.
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

After selecting button that displays alert, following code is used to wait until alert appears:
        timeout_message = 'Timed out waiting for alert message to appear'
        WebDriverWait(support.driver.driver_instance, timeout).until(expected_conditions.alert_is_present(),
                                                                     timeout_message)
"""


class Alert(object):
    """Class for Alert windows"""
    def __init__(self):
        self.__driver = support.driver.driver_instance.switch_to_alert()

    def get_alert_message(self):
        """
        Gets the alert message
        :return: alert message
        """
        logging.info("Get message in alert.")
        alert_message = self.__driver.text
        logging.info("Message in alert is: " + alert_message)
        return alert_message

    def dismiss_alert(self):
        """
        Dismiss alert by selecting cancel button
        :return:
        """
        logging.info('Dismiss alert by selecting \'Cancel\' button.')
        self.__driver.dismiss()

    def accept_alert(self):
        """
        Accept alert by selecting ok button
        :return:
        """
        logging.info('Accept alert by selecting \'OK\' button.')
        self.__driver.accept()
