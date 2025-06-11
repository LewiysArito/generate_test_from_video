from pathlib import Path
from ollama import Client, RequestError, ResponseError
from logs_helper import create_logger
import requests
import settings

logger = create_logger(
    settings.LOG_FILE_TEXT_TO_TEST,
    settings.LOG_LEVEL_TEXT_TO_TEST
)

def get_test_from_text(text_path:Path, test_path:Path):
    """
    Генерация тестов по тексту
    """
    try:
        if test_path.exists():
            logger.warning(f"Вопросы по документу {text_path.name} уже сформированы")
            return 
        
        with open(text_path, "r", encoding="utf-8") as f:
            text_content = f.read()
        prompt = f"""
        На основе следующего текста сгенерируй тестовые вопросы с вариантами ответов:
        Количество текстовых вопросов должно быть от {settings.MIN_COUNT_QUESTIONS}
        до {settings.MAX_COUNT_QUESTIONS}
        ---
        {text_content}
        ---
        Формат: вопрос, 4 варианта ответа, правильный отмечен.
        """
        client = Client(
            host=f'http://{settings.OLLAMA_HOST}:{settings.OLLAMA_PORT}',
        )
        logger.info(f"Отправка запроса к LLM для файла {text_path.name}")
        response = client.generate(model=settings.OLLAMA_MODEL, prompt=prompt)

        with open(test_path, "w", encoding="utf-8") as f:
            f.write(response["response"])
        logger.info(f"Тест сохранён в {test_path.name}")
    except RequestError as e:
        logger.error("Ошибка при запросе в LLM: " + str(e))
    except ResponseError as e:
        logger.error("Ошибка при ответе от LLM: " + str(e))
    except Exception as e:
        logger.error(f"Общая ошибка при обработке {text_path.name}: {e}")

def process():
    """
    Функция для обработки текстовых файлов
    """
    for entry in settings.TEXT_PATH.iterdir():
        file_name = "".join(entry.name.split(".")[:-1])
        test_name = file_name + ".txt"
        test_file_path = settings.TEST_PATH / test_name
        logger.info(f"Обработка файла {entry.name}")
        get_test_from_text(
            text_path=entry,
            test_path=test_file_path
        )
        logger.info(f"Файл {entry.name} обработан")