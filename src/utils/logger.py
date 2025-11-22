# src/utils/logger.py
import logging, os
def get_logger(name='app'):
    logger = logging.getLogger(name)
    if logger.handlers:
        return logger
    logger.setLevel(logging.INFO)
    ch = logging.StreamHandler()
    fmt = '%(asctime)s %(levelname)s [%(name)s] %(message)s'
    ch.setFormatter(logging.Formatter(fmt))
    logger.addHandler(ch)
    # Also log to file
    os.makedirs('logs', exist_ok=True)
    fh = logging.FileHandler('logs/run.log')
    fh.setFormatter(logging.Formatter(fmt))
    logger.addHandler(fh)
    return logger
