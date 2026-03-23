# Temel imaj olarak hafif bir Python sürümü seçiyoruz
FROM python:3.12-slim

# Konteyner içindeki çalışma dizinini belirliyoruz
WORKDIR /code

# Bağımlılık dosyasını kopyalayıp yüklüyoruz
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Uygulama kodlarını kopyalıyoruz
COPY ./app /code/app

# FastAPI'nin çalışacağı portu açıyoruz
EXPOSE 8000

# Uygulamayı başlatma komutu (app/main.py içindeki 'app' objesini hedef alıyoruz)
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]