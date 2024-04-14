import argparse
import cv2
import numpy as np
import os
from tensorflow import keras

# Парсинг аргументов командной строки
parser = argparse.ArgumentParser()
parser.add_argument('model_path', type=str, help='Путь до чекпоинта модели')
parser.add_argument('image_path', type=str, help='Путь до изображения')
args = parser.parse_args()

# Загрузка модели
model = keras.models.load_model(args.model_path)

# Загрузка изображения
image = cv2.imread(args.image_path)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Предобработка изображения
image = cv2.resize(image, (224, 224))
image = image.astype('float32') / 255.0
image = np.expand_dims(image, axis=0)

# Предсказание шрифта
predictions = model.predict(image)
predicted_class = np.argmax(predictions)

# Извлечение информации о классах из генератора данных
train_generator = keras.preprocessing.image.ImageDataGenerator(rescale=1./255)
train_generator = train_generator.flow_from_directory(
    '/content/output_dir/train',
    target_size=(224, 224),
    batch_size=32,
    class_mode='categorical'
)
class_names = list(train_generator.class_indices.keys())

# Вывод результата
predicted_font = class_names[predicted_class]
probability = predictions[0][predicted_class]
print(f'Предсказанный шрифт: {predicted_font}')
print(f'Вероятность: {probability * 100:.2f}%')