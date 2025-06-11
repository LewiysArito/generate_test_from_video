from enum import Enum
from dotenv import load_dotenv
from pathlib import Path
import os
load_dotenv()

# Настройки LLM
OLLAMA_HOST = os.getenv("OLLAMA_HOST", "localhost")
OLLAMA_PORT = int(os.getenv("OLLAMA_PORT", 11434))
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "")

# Папки с файлами
VIDEO_PATH = Path().absolute() / "folder_video"
if not VIDEO_PATH.exists():
    VIDEO_PATH.mkdir()

AUDIO_PATH = Path().absolute() / "folder_audio"
if not AUDIO_PATH.exists():
    AUDIO_PATH.mkdir()

TEXT_PATH = Path().absolute() / "folder_text"
if not TEXT_PATH.exists():
    TEXT_PATH.mkdir()

TEST_PATH = Path().absolute() / "folder_test"
if not TEST_PATH.exists():
    TEST_PATH.mkdir()

# Логи
LOG_PATH = Path().absolute() / "logs"
LOG_FILE_AUDIO_TO_TEXT = LOG_PATH / 'audio_to_text.log'
LOG_FILE_VIDEO_TO_AUDIO = LOG_PATH / 'video_to_audio.log'
LOG_FILE_TEXT_TO_TEST = LOG_PATH / 'text_to_test.log'
LOG_LEVEL_AUDIO_TO_TEXT = os.getenv("LOG_LEVEL_AUDIO_TO_TEXT", 'INFO')
LOG_LEVEL_VIDEO_TO_AUDIO = os.getenv("LOG_LEVEL_VIDEO_TO_AUDIO", 'INFO')
LOG_LEVEL_TEXT_TO_TEST = os.getenv("LOG_LEVEL_TEXT_TO_TEST", 'INFO')

# Параметры генерации тестов
MIN_COUNT_QUESTIONS = int(os.getenv("MIN_COUNT_QUESTIONS", 5))
MAX_COUNT_QUESTIONS = int(os.getenv("MAX_COUNT_QUESTIONS", 10))


