import logging

# Инициализируем логгер
logger = logging.getLogger(__name__)

def square_number(number: int | float):
    logger.debug('Log Debug')
    logger.info('Log Info')
    logger.warning('Log Warning')
    logger.error('Log Error')
    logger.critical('Log Critical')
    
    return number**2