# Objects and related code for the Practice Control Frame
from aut_selenium_framework.demo_site_page import practice_control_frame_ids
from support import common_controls as _ccs
import support.driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time


class PracticeControlFrame(object):
    def __init__(self):
        """
        Practice Control Frame element and related code.
        :return: None
        """
        self.__driver = support.driver.driver_instance
        self.__pc_frame_ids = practice_control_frame_ids

        self.new_browser_window_button = _ccs.Button(self.__driver, 'New Browser Window Button',
                                                     self.__pc_frame_ids.new_browser_window_button_id)
        self.new_message_window_button = _ccs.Button(self.__driver, 'New Message Window Button',
                                                     self.__pc_frame_ids.new_message_window_button_id)
        self.new_browser_tab_button = _ccs.Button(self.__driver, 'Browser Tab Button',
                                                  self.__pc_frame_ids.new_browser_tab_button_id)

        self.alert_box_button = _ccs.Button(self.__driver, 'Alert Box Button',
                                            self.__pc_frame_ids.alert_box_button_id)
        self.timing_alert_button = _ccs.Button(self.__driver, 'Timing Alert Button',
                                               self.__pc_frame_ids.timing_alert_button_id)

        self.change_color_button = _ccs.Button(self.__driver, 'Change Color Button',
                                               self.__pc_frame_ids.change_color_button_id)

    def select_alert_box_button(self, timeout=10):
        """
        Selects the alert box button
        :param timeout: Time to wait for alert to appear
        :return: alert message
        """
        self.alert_box_button.click()
        time.sleep(3)
        timeout_message = 'Timed out waiting for alert message to appear'
        WebDriverWait(support.driver.driver_instance, timeout).until(expected_conditions.alert_is_present(),
                                                                     timeout_message)
        alert = _ccs.Alert()
        return alert
