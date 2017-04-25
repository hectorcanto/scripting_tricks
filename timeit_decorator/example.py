def timeit(func):
    """Wrapper to measure operation."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        log_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        start = time.time()
        return_value = func(*args, **kwargs)
        end = time.time()
        took = end - start
        logger.info(log_time + ": Took {} seconds to change the type of storage to Standard IA, if needed".format(round(took, 2)))
        return return_value
    return wrapper

