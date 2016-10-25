from selenium import webdriver

"""Global interface to web browser"""
driver_instance = None


def initialize():
    """
    Set up driver and create a global driver instance to be
    used throughout.
    :return:
    """
    global driver_instance
    driver_instance = webdriver.Firefox()
    driver_instance.implicitly_wait(10)
    return driver_instance


def close_driver():
    """
    Close out the driver.
    :return:
    """
    global driver_instance
    driver_instance.quit()
