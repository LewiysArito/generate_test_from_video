# Проект: Автоматизация обработки видео, аудио и генерации тестов

## Описание

Этот проект предназначен для автоматизации обработки видеофайлов, извлечения аудио, транскрибации аудио в текст и генерации тестовых вопросов на основе текста с помощью LLM.(например, Ollama).
В итоге это все нужно для создания тестовых вопросов на основе текста или же аудио или же видео

---

## Структура проекта

- `convert_video_to_audio.py` — извлечение аудио из видеофайлов.
- `convert_audio_to_text.py` — транскрибация аудиофайлов в текст с помощью Whisper.
- `convert_text_to_test.py` — генерация тестов по тексту через LLM (Ollama).
- `main.py` — точка входа, запуск задач через CLI.
- `settings.py` — все настройки и пути.
- `logs_helper.py` — вспомогательные функции для логирования.
- `requirement.txt` — зависимости проекта.
- `README.md` — документация (этот файл).
- `.env` — переменные окружения (не коммитить, используйте .env.example).
- `.env.example` — пример файла переменных окружения.
- `folder_video/`, `folder_audio/`, `folder_text/`, `folder_test/` — рабочие папки для файлов.
- `logs/` — папка для логов.

---

## Быстрый старт

1. **Установите зависимости:**
   ```sh
   pip install -r requirement.txt
   ```

2. **Создайте файл .env на основе .env.example и укажите свои параметры.**

3. **Скачать ffmpeg на свою операционную систему, а также скачать Ollama или использовать готовую модель**

4. **Положите видеофайлы в папку `folder_video/`.**

5. **Запустите нужную задачу:**
   ```sh
   python main.py --task convert_video_to_audio
   python main.py --task convert_audio_to_text
   python main.py --task convert_text_to_test
   ```

---

## Описание задач

- `convert_video_to_audio` — извлекает аудиофайлы из всех видео в папке `folder_video/` и сохраняет их в `folder_audio/`.
- `convert_audio_to_text` — транскрибирует все аудиофайлы из `folder_audio/` в текстовые файлы в `folder_text/`.
- `convert_text_to_test` — генерирует тесты по каждому текстовому файлу из `folder_text/` и сохраняет их в `folder_test/`.

---

## Переменные окружения

См. `.env.example` для всех поддерживаемых переменных. Основные:
- `MODEL_NAME` — модель Whisper для транскрибации.
- `FFMPEG_BINARY` — путь к ffmpeg.
- `OLLAMA_HOST`, `OLLAMA_PORT`, `OLLAMA_MODEL` — параметры LLM.
- `LOG_LEVEL_*` — уровни логирования.
- `MIN_COUNT_QUESTIONS`, `MAX_COUNT_QUESTIONS` — диапазон количества вопросов для генерации тестов.

---

## Логирование

Все скрипты ведут логи в папку `logs/` с раздельными файлами для каждого этапа.

---


## Пример запуска

```sh
python main.py --task convert_video_to_audio
python main.py --task convert_audio_to_text
python main.py --task convert_text_to_test
```

---

## Контакты и поддержка

Для вопросов и предложений — создайте issue или обратитесь к автору.
