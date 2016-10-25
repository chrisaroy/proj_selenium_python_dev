# Class for combo boxes
from support.common_controls.__base_element import BaseElement
from selenium.webdriver.support.ui import Select
import support.config as config
import logging
import time


class ComboBox(BaseElement):
    """Common class for combo box elements/widgets"""
    def select_item_by_index(self, index, wait=True, wait_time=config.wait_time):
        """
        Select item by index, or number.
        :param index: Number in combobox to select as integer.  1 will select first item.
        :param wait: True - Wait before performing action
                     False - Do not wait before performing action
        :param wait_time: Time to wait before performing action.
        :return:
        """
        logging.info("Select " + self.name + " by index: " + str(index))
        combobox = Select(self.x_driver.find_element(self.x_elem_id[0], self.x_elem_id[1]))
        if wait:
            time.sleep(wait_time)
        index = (index - 1)  # Adjust for zero based selection.
        combobox.select_by_index(index)

    def select_item_by_value(self, value, wait=True, wait_time=config.wait_time):
        """
        Select item by value.
        :param value: Value in combobox to select.
        :param wait: True - Wait before performing action
                     False - Do not wait before performing action
        :param wait_time: Time to wait before performing action.
        :return:
        """
        logging.info("Select " + self.name + " by value: " + value)
        combobox = Select(self.x_driver.find_element(self.x_elem_id[0], self.x_elem_id[1]))
        if wait:
            time.sleep(wait_time)
        combobox.select_by_value(value)

    def select_item_by_text(self, text, wait=True, wait_time=config.wait_time):
        """
        Select item by the text.
        :param text: Text to select
        :param wait: True - Wait before performing action
                     False - Do not wait before performing action
        :param wait_time: Time to wait before performing action.
        :return:
        """
        logging.info("Select " + self.name + " by text: " + text)
        combobox = Select(self.x_driver.find_element(self.x_elem_id[0], self.x_elem_id[1]))
        if wait:
            time.sleep(wait_time)
        combobox.select_by_visible_text(text)

    def get_all_items(self, log_items=True, wait=True, wait_time=config.wait_time):
        """
        Get all items
        :param log_items: True - Prints out a log of all items in list.
                          False - Does not print out log of all items in list.
        :param wait: True - Wait before performing action
                     False - Do not wait before performing action
        :param wait_time: Time to wait before performing action.
        :return: list of all items
        """
        logging.info("Get selected item from: " + self.name)
        combobox = Select(self.x_driver.find_element(self.x_elem_id[0], self.x_elem_id[1]))
        if wait:
            time.sleep(wait_time)
        all_items = combobox.options
        if len(all_items) == 0:
            return None
        logging.info('There are ' + str(len(all_items)) + ' items in ' + self.name)
        items = [x.text for x in all_items]
        if log_items:
            logging.info('Items in ' + self.name + ' combobox: ')
            for option in items:
                logging.info("    " + option)

        return items

    def get_selected_item(self, wait=True, wait_time=config.wait_time):
        """
        Get selected item
        :param wait: True - Wait before performing action
                     False - Do not wait before performing action
        :param wait_time: Time to wait before performing action.
        :return: selected item
        """
        logging.info("Get selected item from: " + self.name)
        combobox = Select(self.x_driver.find_element(self.x_elem_id[0], self.x_elem_id[1]))
        if wait:
            time.sleep(wait_time)
        selected_item = combobox.first_selected_option
        logging.info("Selected item from " + self.name + " is \'" + selected_item.text + "\'")
        return selected_item.text
