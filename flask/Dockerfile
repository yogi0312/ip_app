FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1 \
	PYTHONDONTWRITEBYTECODE=1 \

WORKDIR /app

# Copy requirements first for better layer caching
COPY requirements.txt .

# Install Python deps (no cache)
RUN pip install --no-cache-dir -r requirements.txt

# Copy app sources
COPY . .

# Create non-root user and give ownership of app directory
RUN useradd --create-home --shell /bin/bash appuser \
 && chown -R appuser:appuser /app
USER appuser

EXPOSE 5000

CMD ["python", "app.py"]