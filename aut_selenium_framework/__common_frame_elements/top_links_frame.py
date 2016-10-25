# Objects and related code for the Top Links frame
from aut_selenium_framework.__common_frame_elements import top_links_frame_ids
from support import common_controls as _ccs
import support.driver


class TopLinksFrame(object):
    def __init__(self):
        """
        Top links frame elements and related code.
        :return: None
        """
        self.__driver = support.driver.driver_instance
        self.__tl_frame_ids = top_links_frame_ids

        self.home_link_button = _ccs.Button(self.__driver, 'Home Link Button', self.__tl_frame_ids.home_link_button_id)
        self.tutorial_link_button = _ccs.Button(self.__driver, 'Tutorial Link Button',
                                                self.__tl_frame_ids.tutorial_link_button_id)
        self.about_link_button = _ccs.Button(self.__driver, 'About Link Button',
                                             self.__tl_frame_ids.about_link_button_id)
        self.contact_link_button = _ccs.Button(self.__driver, 'Contact Link Button',
                                               self.__tl_frame_ids.contact_link_button_id)
