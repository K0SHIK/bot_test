import logging

# Инициализируем логгер
logger = logging.getLogger(__name__)

# Определяем свой фильтр от класса Filter
class CriticalLogFilter(logging.Filter):
    # переопределяем метод filter
    def filter(self, record):
        return record.levelname == 'CRITICAL'
    
# Инициализируем форматтер
formatter_3 = logging.Formatter(fmt='#%(levelname)-8s [%(asctime)s] - %(message)s')

# Инициализируем первый хэндлер который будет писать в stderr
stderr = logging.StreamHandler()
# Инициализируем второй хэндлер который будет писать в critical.log
critical_file = logging.FileHandler('critical.log', mode='w', encoding='utf-8')
        
# Определяем форматирование логов во втором хэндлере
critical_file.setFormatter(fmt=formatter_3)
# Добавляем фторому хэндлеру фильтр
critical_file.addFilter(CriticalLogFilter())
# Добавляем хэндлеры к логгеру
logger.addHandler(stderr)
logger.addHandler(critical_file)

def square_number(number: int | float):
    logger.debug('Log Debug')
    logger.info('Log Info')
    logger.warning('Log Warning')
    logger.error('Log Error')
    logger.critical('Log Critical')
    
    return number**2