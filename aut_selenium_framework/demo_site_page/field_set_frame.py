# Objects and related code for the Field Set Frame
from aut_selenium_framework.demo_site_page import field_set_frame_ids
from support import common_controls as _ccs
import support.driver


class ComboBoxConstants:
    OPTION_1 = 'Option 1'
    OPTION_2 = 'Option 2'
    OPTION_3 = 'Option 3'


class FieldSetFrame(object):
    def __init__(self):
        """
        Field Set Frame elements and related code.
        :return: None
        """
        self.__driver = support.driver.driver_instance
        self.__fs_frame_ids = field_set_frame_ids
        self.select_combo_box_constants = ComboBoxConstants

        self.text_area_text_area = _ccs.TextArea(self.__driver, 'Text area - Text area',
                                                 self.__fs_frame_ids.text_area_text_area_id)
        self.textbox_textbox = _ccs.TextBox(self.__driver, 'Textbox - Textbox',
                                            self.__fs_frame_ids.text_box_text_box_id)

        self.option_1_checkbox = _ccs.CheckBox(self.__driver, 'Option 1 Checkbox',
                                               self.__fs_frame_ids.option_1_checkbox_id)
        self.option_2_checkbox = _ccs.CheckBox(self.__driver, 'Option 2 Checkbox',
                                               self.__fs_frame_ids.option_2_checkbox_id)
        self.option_3_checkbox = _ccs.CheckBox(self.__driver, 'Option 3 Checkbox',
                                               self.__fs_frame_ids.option_3_checkbox_id)

        self.option_1_radio_button = _ccs.RadioButton(self.__driver, 'Option 1 Radio Button',
                                                      self.__fs_frame_ids.option_1_radio_button_id)
        self.option_2_radio_button = _ccs.RadioButton(self.__driver, 'Option 2 Radio Button',
                                                      self.__fs_frame_ids.option_2_radio_button_id)
        self.option_3_radio_button = _ccs.RadioButton(self.__driver, 'Option 3 Radio Button',
                                                      self.__fs_frame_ids.option_3_radio_button_id)
        self.select_combo_box = _ccs.ComboBox(self.__driver, 'Select Combobox', self.__fs_frame_ids.select_combo_box_id)
