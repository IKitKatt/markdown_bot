__version__ = "1.0.0"
__all__ = ["main"]  # Какие модули экспортировать при импорте *

# Инициализация логгера
import logging
logging.getLogger(__name__).addHandler(logging.NullHandler())