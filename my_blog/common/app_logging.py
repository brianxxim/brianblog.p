import logging
import os
from logging import Logger
from logging.handlers import RotatingFileHandler


def create_logger():
    """
    创建日志器 (已废弃)
    :return: 日志器
    """
    # log_file_name = settings.LOGGING_FILE_NAME
    # log_file_path = settings.LOGGING_FILE_PATH
    # log_max_bytes = settings.LOGGING_MAX_BYTES
    # log_backup_count = settings.LOGGING_BACKUP_COUNT
    log_file_name = 'blog.log'
    log_file_path = os.path.dirname(__name__)
    log_max_bytes = 100 * 1024 * 1024
    log_backup_count = 3
    handler = logging.handlers.RotatingFileHandler(os.path.join(log_file_path, log_file_name),
                                                   maxBytes=log_max_bytes,
                                                   backupCount=log_backup_count,
                                                   encoding='utf-8')

    formatter = logging.Formatter('%(levelname)s: [%(asctime)s]  '
                                  '%(pathname)s, line %(lineno)d, in %(funcName)s \n  "%(message)s"')
    handler.setFormatter(formatter)

    _logger: Logger = logging.getLogger('django')
    _logger.addHandler(handler)
    _logger.setLevel(logging.INFO)

    return _logger


def create_logger_test():
    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(levelname)s: [%(asctime)s]  '
                                  '%(pathname)s, line %(lineno)d, in %(funcName)s \n  "%(message)s"')
    handler.setFormatter(formatter)

    _logger = create_logger()
    _logger.addHandler(handler)
    return _logger


def func():
    try:
        1 / 0
    except Exception as e:
        logger.debug('debug')
        logger.info('info')
        logger.warning('warning')
        logger.error('error')
        logger.critical('critical')


if __name__ == '__main__':
    logger = create_logger_test()
    func()
