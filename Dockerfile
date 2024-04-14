# Используем базовый образ TensorFlow
FROM tensorflow/tensorflow:latest-gpu

# Установка OpenCV
RUN apt-get update && \
    apt-get install -y libsm6 libxext6 libxrender-dev && \
    pip install opencv-python

# Установка других необходимых библиотек
RUN pip install numpy

# Копирование кода приложения
COPY font_recognition.py /app/

# Рабочая директория
WORKDIR /app

# Запуск приложения по умолчанию (можно переопределить при запуске контейнера)
CMD ["python", "font_recognition.py", "/path/to/model/checkpoint", "/path/to/image/file"]