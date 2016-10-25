from datetime import datetime
import logging
import time
import support.config
import support.driver


def setup(test_name):
    """
    Method to call at the start of a test.
    :param test_name: Name of test
    :return: None
    """
    support.config.test_name = test_name
    # support.config.start_time = datetime.now()
    logging.info('* Start Test: ' + test_name)


def cleanup():
    """
    Method to all at end of test.
    :return: None
    """
    logging.info('')
    logging.info('* End Test: ' + support.config.test_name)
    test_summary()


def sleep(sleep_seconds):
    """
    Sleep/snooze for specified time in seconds
    :param sleep_seconds: Number of seconds to sleep/snooze
    :return: None
    """
    time.sleep(sleep_seconds)
    logging.info('Sleep for %d seconds.', sleep_seconds)


def take_image(image_name='image'):
    """
    Take and image at existing are of application.
    :param image_name: name of image
    :return:
    """
    current_time = datetime.now().strftime('%Y_%m_%d %H-%M-%S %p - ')
    filename = support.config.test_log_folder + current_time + image_name + '.png'
    support.driver.driver_instance.get_screenshot_as_file(filename)
    logging.info('Take image and store to: ' + filename)


def test_step(step_summary):
    """
    Add log statement for test step and track number of steps
    :param step_summary:
    :return:
    """
    support.config.test_step += 1
    logging.info('')
    logging.info("Start Test Step: %s - %s", str(support.config.test_step), step_summary)


def test_summary():
    """
    Adds summary of test to test log.
    :return:
    """
    logging.info('')
    # logging.info('Test Duration: ', support.config.duration)
    logging.info('')
    logging.info('TEST SUMMARY:')
    logging.info('  Test Name: %s', support.config.test_name)
    logging.info('  Test Steps: %s', support.config.test_step)
    logging.info('  Verification:')
    logging.info('    Passed: %s', support.config.number_passes)
    logging.info('    Failed: %s', support.config.number_fails)
    logging.info('    Total: %s', support.config.number_verifications)
    logging.info('')
    logging.info('Test log location %s', support.config.test_log_folder)
