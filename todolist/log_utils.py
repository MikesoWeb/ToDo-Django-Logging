import logging
import os

from django.conf import settings
from django.utils import timezone



# Создаем директорию logs, если она не существует
if not os.path.exists(settings.LOGS_DIR):
    os.makedirs(settings.LOGS_DIR)


def setup_log_handler(logger, filename, encoding='utf-8'):
    log_handler = logging.FileHandler(
        os.path.join(settings.LOGS_DIR, filename), encoding=encoding)
    logger.addHandler(log_handler)


# Создаем логгеры
create_logger = logging.getLogger('create_logger')
update_logger = logging.getLogger('update_logger')
delete_logger = logging.getLogger('delete_logger')
error_logger = logging.getLogger('error_logger')


# Настраиваем обработчики логов
setup_log_handler(create_logger, 'create.log')
setup_log_handler(update_logger, 'update.log')
setup_log_handler(delete_logger, 'delete.log')
setup_log_handler(error_logger, 'error.log')


# Функция для логгирования событий
def log_event(logger_name, message):
    now = timezone.localtime(timezone.now())
    formatted_time = now.strftime('%d %B %Y %H:%M:%S')
    logger = logging.getLogger(logger_name)
    log_message = f'{formatted_time} - {message}'

    try:
        with open(logger.handlers[0].baseFilename, 'a', encoding='utf-8') as log_file:
            log_file.write(log_message + '\n')
    except Exception as e:
        # Обработка ошибок записи в файл логов
        print(f'{formatted_time} - {e}')
        error_message = f'{formatted_time} - {e}'
        error_logger.error(error_message)
