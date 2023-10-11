# Используем базовый образ Python 3.11
FROM python:3.11-slim-buster

# Устанавливаем переменную окружения для отключения вывода буферизации
ENV PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=random \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100

# Устанавливаем poetry
RUN pip install poetry

# Копируем файлы зависимостей в контейнер
COPY pyproject.toml poetry.lock ./

# Устанавливаем зависимости
RUN poetry install

# Копируем все файлы проекта в контейнер
COPY . .

EXPOSE 8000

RUN poetry run python ./manage.py migrate

# Запускаем команду для запуска Gunicorn сервера
CMD ["poetry", "run", "gunicorn", "--bind", "0.0.0.0:8000", "core.wsgi:application"]