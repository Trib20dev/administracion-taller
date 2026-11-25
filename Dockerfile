FROM python:3.12-slim

# Evita archivos .pyc y permite ver los logs de uvicorn al instante
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# 1. Instalar dependencias primero (aprovecha la caché de Docker)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 2. Copiar solo el código fuente necesario para el servidor
COPY src/ ./src/

# Exponer el puerto de FastAPI
EXPOSE 8000

# Arrancar uvicorn escuchando en 0.0.0.0 (obligatorio dentro de Docker)
CMD ["uvicorn", "servidor.api:app", "--host", "0.0.0.0", "--port", "8000", "--app-dir", "src"]