# Objects and related code for the Contact Us Frame
from aut_selenium_framework.demo_site_page import contact_us_frame_ids
from support import common_controls as _ccs
import support.driver


class ContactUsFrame(object):
    def __init__(self):
        """
        Contact Us Frame elements and related code.
        :return: None
        """
        self.__driver = support.driver.driver_instance
        self.__cu_frame_ids = contact_us_frame_ids

        self.telephone_textbox = _ccs.TextBox(self.__driver, 'Telephone Textbox',
                                              self.__cu_frame_ids.telephone_textbox_id)
