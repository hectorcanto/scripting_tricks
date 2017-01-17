import logging
from configure_log import set_stdout_logging


logger = set_stdout_logging("example", log_level=logging.DEBUG)

def example():

    logger.debug("Debug message")
    logger.info("Info message")
    logger.error("Error message")

    try:
        raise TypeError
    except TypeError as e:
        logger.exception("This logs an Exception but let the program continue. Be careful")

if __name__ == "__main__":
    example()