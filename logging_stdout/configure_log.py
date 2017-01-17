import sys
import logging


def set_stdout_logging(module_name=None, log_level=logging.INFO):
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
    handler.setLevel(log_level)

    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG) # You have to set both logger and handler log level

    return logger