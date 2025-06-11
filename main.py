import argparse
import sys
from convert_audio_to_text import process as convert_audio_to_text_process
from convert_video_to_audio import process as convert_video_to_audio_process
from convert_text_to_test import process as convert_text_to_test_process
CHOICES_TASKS = [
    "convert_audio_to_text",
    "convert_video_to_audio",
    "convert_text_to_test"
]

def create_parser()->argparse.ArgumentParser:
    """
    Создает парсер
    """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-m", "--task",
        required=True,
        choices=CHOICES_TASKS,
        help="Список задач для запуска"
    )
    return parser

def task_runner(task: str):
    """
    Запуск задач
    """
    match task:
        case "convert_audio_to_text":
            return convert_audio_to_text_process()
        case "convert_video_to_audio":
            return convert_video_to_audio_process()
        case "convert_text_to_test":
            return convert_text_to_test_process()
        case _:
            raise ValueError(f"Задача должна быть из следующего пула: {",".join(CHOICES_TASKS)}")

if __name__ == "__main__":
    parser = create_parser()
    args = parser.parse_args()
    result = task_runner(args.task)
