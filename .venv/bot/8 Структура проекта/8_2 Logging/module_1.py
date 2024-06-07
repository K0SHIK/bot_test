import logging

from module_2 import divide_number
from module_3 import square_number
# Инициализируем логер
logger = logging.getLogger(__name__)
# Устанавливаем логеру уровень DEBUG
logger.setLevel(logging.DEBUG)

# Определяем свой фильтр, наследуясь от класса Filter библиотеки logging
class ErrorLogFilter(logging.Filter):
    # Переопределяем метод filter, переменная рекорд будет ссылаться на объект класса LogRecord
    def filter(self, record):
        return record.levelname == 'ERROR'

# Инициализируем форматтер
formatter_1 = logging.Formatter(fmt='[%(asctime)s] #%(levelname)-8s %(filename)s:'
                                    '%(lineno)d - %(name)s:%(funcName)s - %(message)s')

# Инициализируем хэндлер которвый будет писать логи
error_file = logging.FileHandler('error.log', 'w', encoding='utf-8')
# Устанавливаем уровень DEBUG
error_file.setLevel(logging.DEBUG)
# Добавляем хэндлеру фильтер ErrorLogFilter, который будет пропускать логи уровня ERROR
error_file.addFilter(ErrorLogFilter())
# Определяем форматирование
error_file.setFormatter(formatter_1)
#Добавляем хэндлер в логгер
logger.addHandler(error_file)

def main():
    a, b = 12, 2
    c, d = 4, 0

    logger.debug('Лог DEBUG')
    logger.info('Лог INFO')
    logger.warning('Лог WARNING')
    logger.error('Лог ERROR')
    logger.critical('Лог CRITICAL')

    print(divide_number(a, square_number(b)))
    print(divide_number(square_number(c), d))