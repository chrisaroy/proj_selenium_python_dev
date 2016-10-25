#!/usr/bin/python
import unittest
from datetime import datetime
import os
import logging
import time

import aut_selenium_framework
import support
import support.shared as shared

"""
Copyright (C) 2016 - All Rights Reserved
"""
######################################################
test_name = 'Basic Test'

manual_test_version = '.1'

summary = 'Basic Selenium test written in Python using POM (Page Object Model) and EOM (Element Object Model.'

requirement = ['req-123', 'req-321', 'req-444']

manual_test_time = 30

test_log_location = '../../test_results/'
######################################################

support.config.test_name = test_name
support.config.test_log_folder = support.config.test_logs_location + datetime.now().strftime('%Y_%m_%d %H-%M-%S %p - ')\
                                 + test_name + '/'
os.makedirs(support.config.test_log_folder)
support.test_log.TestLog()

website = 'http://www.seleniumframework.com/Practiceform/'


# Tests
class SeleniumPractice(unittest.TestCase):

    def setUp(self):
        shared.setup(test_name)
        support.driver.initialize()

    def tst_field_set_frame(self):
        """
        Test various elements in the Field Set Frame of the Demo Site.
        :return: None
        """
        shared.take_image('field_set_frame')
        shared.sleep(3)
        field_set_frame = aut_selenium_framework.demo_site_page.field_set_frame()

        # Text area
        field_set_frame.text_area_text_area.clear_text()
        field_set_frame.text_area_text_area.enter_text('Line 1', clear_text=False)
        field_set_frame.text_area_text_area.select_return()
        field_set_frame.text_area_text_area.enter_text('Line 2', clear_text=False)

        # Text Box
        field_set_frame.textbox_textbox.enter_text('20 Mile March')
        actual_text = field_set_frame.textbox_textbox.get_text()

        support.verify(description='Check text in textbox',
                       actual=actual_text,
                       expected='Mile',
                       requirements='req-123')
        time.sleep(2)

        # Checkboxes
        op_1_checked = field_set_frame.option_1_checkbox.is_checked()
        support.verify(description='Check option 1 checked',
                       actual=op_1_checked,
                       expected=False)
        time.sleep(2)
        field_set_frame.option_3_checkbox.select()
        time.sleep(2)

        # Radio button
        field_set_frame.option_2_radio_button.select()
        op_2_selected = field_set_frame.option_2_radio_button.is_selected()
        support.verify(description='Option 2 radio button selected',
                       actual=op_2_selected,
                       expected=True)
        time.sleep(2)

        # Combobox
        field_set_frame.select_combo_box.select_item_by_text(field_set_frame.select_combo_box_constants.OPTION_2)
        field_set_frame.select_combo_box.select_item_by_value('Option 1')
        field_set_frame.select_combo_box.select_item_by_index(3)
        selected_item = field_set_frame.select_combo_box.get_selected_item()
        support.verify(description='Check selected item.',
                       actual=selected_item,
                       expected=field_set_frame.select_combo_box_constants.OPTION_3)
        time.sleep(2)

        all_items = field_set_frame.select_combo_box.get_all_items()
        logging.info('Items in combobox are: ' + all_items[0] + ', ' + all_items[1] + ', ' + all_items[2])

        logging.info('wait here.')

    def tst_practice_control_frame(self):
        """
        Test various elements in the Practice Control Frame of the Demo Site.
        :return:
        """
        shared.take_image('practice_control_frame')
        practice_control_frame = aut_selenium_framework.demo_site_page.practice_control_frame()

        # Alert Box
        # TODO: Determine timing issue and remove extra 'sleep' statements
        """
        alert = practice_control_frame.select_alert_box_button()
        time.sleep(4)
        alert.get_alert_message()
        time.sleep(3)
        alert.accept_alert()
        """

        practice_control_frame.change_color_button.click(wait_time=3)
        support.verify(description='Check text in color button',
                       actual=practice_control_frame.change_color_button.get_text(),
                       expected='Change Color',
                       requirements='req-231')

    def tst_contact_us_frame(self):
        """
        Test various elements in the Contact Us Frame of the Demo Site.
        :return:
        """
        shared.take_image('get_text_frame')
        contact_us_frame = aut_selenium_framework.demo_site_page.contact_us_frame()
        contact_us_frame.telephone_textbox.enter_text('867-5309')
        support.verify(description='Check phone number',
                       actual=contact_us_frame.telephone_textbox.get_text(),
                       expected='867-5309')

    # MAIN
    def test_search_in_python_org(self):
        support.driver.driver_instance.get(website)
        self.assertIn('Selenium Framework', support.driver.driver_instance.title)

        # Test Step 1
        shared.test_step('Test the field set frame')
        self.tst_field_set_frame()

        # Test Step 2
        shared.test_step('Test the practice control frame')
        self.tst_practice_control_frame()

        # Test Step 3
        shared.test_step('Test the Contact us frame')
        self.tst_contact_us_frame()

        shared.take_image('end_test')
        logging.info('End of Test')

    def tearDown(self):
        shared.cleanup()
        support.driver.close_driver()

if __name__ == "__main__":
    unittest.main()
