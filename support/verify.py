import support.config
import support.shared
import logging


def verify(description, actual, expected, requirements=None, capture_window_image=True):
    """
    Compare actual vs expected and enter information into log.
    :param description: Description of verification
    :param actual: Actual result
    :param expected: Expected result
    :param requirements: Requirement(s) tested
    :param capture_window_image: True - Take screen image at verification point.
                                 False - Do not take image at verification point.
    :return: result - Pass - If actual and expected match.
                      Fail - If actual and expected do not match
    """
    support.config.image_number += 1
    support.config.number_verifications += 1
    verify_image_name = "screen_capture_" + str(support.config.image_number) + "_verify "

    if actual == expected:
        result = 'PASS'
        support.config.number_passes += 1
    else:
        result = 'FAIL'
        support.config.number_fails += 1

    if capture_window_image:
        support.shared.take_image(verify_image_name)

    logging.info('VERIFY: %s', description)
    logging.info('  Result: %s', result)
    logging.info('  actual: %s', actual)
    logging.info('  expected: %s', expected)
    if requirements is not None:
        logging.info('  Requirements: %s', requirements)
    if capture_window_image is not False:
        logging.info('  Verification screen capture: %s', verify_image_name)

    return result
