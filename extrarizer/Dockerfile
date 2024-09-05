# Этап 1: Установка зависимостей Python и сборка приложения
FROM python:3.12-slim AS builder

WORKDIR /app

# Копируем файлы для установки зависимостей
COPY requirements.txt requirements.txt

# Устанавливаем Python-зависимости
RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc && \
    pip install --no-cache-dir -r requirements.txt && \
    rm -rf /root/.cache/pip && \
    apt-get purge -y --auto-remove gcc && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Этап 2: Создание финального образа
FROM python:3.12-slim

WORKDIR /app

# Копируем зависимости и исходный код из первого этапа
COPY --from=builder /usr/local/lib/python3.12/site-packages/ /usr/local/lib/python3.12/site-packages/
COPY . .

ENV HOST=0.0.0.0
ENV PORT=8000
# Это отключает генерацию файлов с расширением .pyc (байт-код Python), которые обычно создаются при компиляции Python-файлов.
# Это полезно для уменьшения объема файлов в контейнере и ускорения работы с файлами.
ENV PYTHONDONTWRITEBYTECODE=1
# Отключает буферизацию вывода в Python, что заставляет вывод (например, print или logging) сразу же отображаться в консоли, а не кэшироваться.
ENV PYTHONUNBUFFERED=1

EXPOSE $PORT

# Запуск приложения
ENTRYPOINT ["python3", "main.py"]
CMD ["--host", "$HOST", "--port", "$PORT"]
