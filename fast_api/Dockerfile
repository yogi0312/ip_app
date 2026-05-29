FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN useradd --create-home --shell /bin/bash appuser \
 && chown -R appuser:appuser /app
USER appuser

EXPOSE 5000

CMD ["fast_api", "run", "app.py", "--host", "0.0.0.0", "--port", "5000"]
