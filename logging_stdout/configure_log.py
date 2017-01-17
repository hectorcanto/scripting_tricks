import sys
import logging
from default_configuration import GENERAL_LOG_LEVEL


def set_stdout_logging(module_name=None, log_level=logging.INFO, set_general_log=False):
    """
    Args:
        module_name (str): sets the logging sub-module,
        log_level (int): logging standard values 10, 20, 30 ,40, 50. Use logging constants for clarity

    Returns:
        The configured logged
    """

    logger = logging.getLogger(module_name) if module_name else logging.getLogger()
    handler = logging.StreamHandler(stream=sys.stdout)

    formatter = logging.Formatter("[%(levelname)s] %(asctime)s - %(name)s - %(message)s")
    handler.setFormatter(formatter)
    handler.setLevel(log_level) # You have to set both logger and handler log level

    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)
    if set_general_log:
        set_general_log_level()

    return logger


def set_general_log_level():
    """
    You only need to run this once in your script, but if you run it several times, the last one will be the definitive.
    """

    root_logger = logging.getLogger()
    root_logger.setLevel(GENERAL_LOG_LEVEL)
