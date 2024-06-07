import logging
import sys

# Инициализируем логгер модуля
logger = logging.getLogger(__name__)

# Определяем свой фильтр, наследуясь от класса Filter в библиотеке logging
class DebugWarningLogFilter(logging.Filter):
    # Переопределяем метод filner, переменная record будет ссылаться на объект класса LogRecord
    def filter(self, record):
        return record.levelname in ('DEBUG', 'WARNING')

# Инициализируем форматтер
formatter_2 = logging.Formatter(fmt='#%(levelname)-8s [%(asctime)s] - %(filename)s:'
                                    '%(lineno)d - %(name)s:%(funcName)s - %(message)s')

# Инициализируем хэндлер, который будет писать логи в stdout
stdout = logging.StreamHandler(sys.stdout)

# Добавляем хэндлеру фильр ebugWarningLogFilter
stdout.addFilter(DebugWarningLogFilter())

# Определяем форматирование логов в хэндлере
stdout.setFormatter(formatter_2)

# Добавляем хэндлер к логгеру
logger.addHandler(stdout)

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