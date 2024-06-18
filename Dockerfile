# Usar una imagen base oficial de Python
FROM python:3.8-slim

# Instalar dependencias del sistema para psycopg2
RUN apt-get update && apt-get install -y libpq-dev gcc

# Establecer el directorio de trabajo en el contenedor
WORKDIR /app

# Copiar el archivo de requerimientos y instalar las dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del código fuente del proyecto al contenedor
COPY . .

# Exponer el puerto 8000 para acceder al servidor web
EXPOSE 8000

# Comando para ejecutar la aplicación usando Gunicorn como servidor WSGI
CMD ["gunicorn", "--chdir", "gest_stock", "gest_stock.wsgi:application", "--bind", "0.0.0.0:8000"]
