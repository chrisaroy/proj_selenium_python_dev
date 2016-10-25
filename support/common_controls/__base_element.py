# Base class for all widgets/elements
import logging


class BaseElement(object):
    """Common base class for al widgets/elements"""
    def __init__(self, driver, name, elem_id):
        """
        Common code for all elements/widgets.
        :param driver: Interface to Website
        :param elem_id: Unique ID related to the element
        :return: None
        """
        self.x_driver = driver
        self.name = name
        self.x_elem_id = elem_id

    def is_enabled(self):
        """
        Determine if the element is enabled.
        :return: True if enabled
                 False if not enabled
        """
        logging.info('Determine if ' + self.name + ' is enabled.')
        element = self.x_driver.find_element(self.x_elem_id[0], self.x_elem_id[1])
        enabled = element.is_enabled()
        logging.info('Enabled state of ' + self.name + ' is: ' + str(enabled))
        return enabled

    def is_visible(self):
        """
        Determine if the element is visible/displayed.
        :return: True if visible/displayed
                 False if not visible/displayed
        """
        logging.info('Determine if ' + self.name + ' is visible.')
        element = self.x_driver.find_element(self.x_elem_id[0], self.x_elem_id[1])
        visible = element.is_displayed()
        logging.info('Visible state of ' + self.name + ' is: ' + str(visible))
        return visible
