import logging
import sys

# Инициализируем логгер модуля
logger = logging.getLogger(__name__)

def divide_number(dividend: int | float, devider: int | float):
    logger.debug('Log Debug')
    logger.info('Log Info')
    logger.warning('Log Warning')
    logger.error('Log Error')
    logger.critical('Log Critical')
    
    try:
        return dividend / devider
    except ZeroDivisionError:
        logger.exception('Произошло деление на 0')