import settings
from moviepy import VideoFileClip
from pathlib import Path
from logs_helper import create_logger

logger = create_logger(
    settings.LOG_FILE_VIDEO_TO_AUDIO,
    settings.LOG_LEVEL_VIDEO_TO_AUDIO
)

def extract_audio(video_path:Path, audio_path:Path):
    """
    Извлекает аудио из видео.

    Args:
        video_path: Путь к видеофайлу.
        audio_path: Путь для сохранения аудиофайла.
    """
    try:
        logger.info(f"Начало извлечения аудио из {video_path.name}")
        clip = VideoFileClip(str(video_path.absolute()))
        clip.audio.write_audiofile(str(audio_path.absolute()),logger=None)
        clip.close()
        video_path.unlink()
        logger.info(f"Аудио {video_path.name} извлечено успешно!")
    except Exception as e:
        logger.error(f"Ошибка при извлечении аудио {video_path.name}: {e}")

def process():
    """
    Функция для обработки видеофайлов
    """
    for entry in settings.VIDEO_PATH.iterdir():
        file_name = "".join(entry.name.split(".")[:-1])
        audio_file_name = file_name + ".mp3"
        audio_file_path = settings.AUDIO_PATH / audio_file_name
        logger.info(f"Обработка файла {entry.name}")
        extract_audio(
            video_path=entry, 
            audio_path=audio_file_path
        )
        logger.info(f"Файл {entry.name} обработан")

