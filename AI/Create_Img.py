# pip install Pillow


import os
from sklearn import datasets
from PIL import Image
import numpy as np

# 1. Загружаем данные
digits = datasets.load_digits()

# 2. Создаем папку для картинок, если её нет
output_dir = "digits_images"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

print(f"Начинаю сохранение {len(digits.images)} изображений...")

# 3. Проходим циклом по всем картинкам
for i, (image, target) in enumerate(zip(digits.images, digits.target)):
    # Данные в датасете идут от 0 до 16.
    # Для стандартного ч/б изображения (L) нужно привести их к диапазону 0-255.
    # Инвертируем (16 - image), чтобы цифры были черными на белом фоне (так привычнее)
    rescaled = ((16 - image) / 16 * 255).astype(np.uint8)

    # Создаем объект изображения
    img = Image.fromarray(rescaled, mode='L')

    # Увеличим картинку, чтобы её было удобно смотреть (с 8x8 до 80x80)
    # Используем Image.NEAREST, чтобы не было размытия
    img = img.resize((80, 80), resample=Image.NEAREST)

    # Сохраняем файл. В названии укажем индекс и что это за цифра
    filename = f"digit_{i}_is_{target}.png"
    img.save(os.path.join(output_dir, filename))

print(f"Готово! Все картинки сохранены в папку: {os.path.abspath(output_dir)}")