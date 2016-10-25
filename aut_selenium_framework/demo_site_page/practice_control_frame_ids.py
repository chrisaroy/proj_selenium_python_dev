# ID file for the Practice Control Frame
from selenium.webdriver.common.by import By

# Browser Windows
new_browser_window_button_id = [By.ID, 'button1']
new_message_window_button_id = [By.XPATH, '//button[@onclick=\'newMsgWin()\']']  # NEED TO CHECK
new_browser_tab_button_id = [By.XPATH, '//button[@onclick=\'newBrwTab()\']']

alert_box_button_id = [By.ID, 'alert']
timing_alert_button_id = [By.ID, 'timingAlert']

change_color_button_id = [By.ID, 'colorVar']
