import os
import whisper
import settings
from logs_helper import create_logger
from pathlib import Path

logger = create_logger(
    settings.LOG_FILE_AUDIO_TO_TEXT,
    settings.LOG_LEVEL_AUDIO_TO_TEXT
)

def extract_text(audio_path:Path, text_path:Path):
    """
    Извлекает аудио из видео.

    Args:
        audio_path: Путь к аудиофайлу
        text_path: Путь для сохранения текста файла
    """
    try:
        model = whisper.load_model(name=os.getenv("MODEL_NAME", "medium"))
        logger.info(f"Начало трансгрибации для файла {audio_path}")
        result = model.transcribe(str(audio_path.absolute()), fp16=False)
        logger.info(f"Конец трансгрибации файла для {audio_path}")
        with open(text_path, "w") as f:
            f.write(result["text"])
        
        audio_path.unlink()
        logger.info(f"Был записан текст {text_path}")
    except Exception as e:
        logger.error("Не удалось преобразовать аудио {audio_path} в текст " + str(e))

def process():
    """
    Функция для обработки аудиофайлов
    """
    for entry in settings.AUDIO_PATH.iterdir():
        file_name = "".join(entry.name.split(".")[:-1])
        text_file_name = file_name + ".txt"
        text_file_path = settings.TEXT_PATH / text_file_name

        extract_text(
            audio_path=entry, 
            text_path=text_file_path
        )
        logger.info(f"Файл {entry.name} обработан")
