from enum import Enum
import logging
from pathlib import Path
from typing import Optional

# Настройка уровней логирования
class LogLevel(Enum):
    INFO = logging.INFO
    WARNING = logging.WARNING
    ERROR = logging.ERROR
    DEBUG = logging.DEBUG
    CRITICAL = logging.CRITICAL

def parse_log_level(level_str: str) -> LogLevel:
    """
    Преобразует строку в соответствующий LogLevel.
    """
    try:
        return LogLevel[level_str.upper()].value
    except KeyError:
        raise ValueError(f"Некорректный уровень логирования: {level_str}. \
                         Допустимые значения: {', '.join(LogLevel.__members__.keys())}")

def create_logger(
        log_path: Path,
        log_level: LogLevel = LogLevel.INFO,
        logger_name: Optional[str] = None
    ) -> logging.Logger:
    """
    Создаёт и настраивает логгер.
    log_path: путь к файлу лога
    log_level: уровень логирования (LogLevel)
    logger_name: имя логгера (по умолчанию root)
    """
    log_path.parent.mkdir(parents=True, exist_ok=True)
    logger = logging.getLogger(logger_name)
    logger.setLevel(parse_log_level(log_level))
    formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s')

    if logger.hasHandlers():
        logger.handlers.clear()
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    file_handler = logging.FileHandler(log_path, encoding='utf-8')
    file_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)
    logger.addHandler(file_handler)
    
    return logger