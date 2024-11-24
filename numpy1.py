import numpy as np
import cv2
from matplotlib import pyplot as plt

# Загрузим изображение в оттенках серого
image_path = r'C:\Users\dimab\OneDrive\Desktop\lunar_images\lunar03_raw.jpg'
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Найдем минимальные и максимальные значения пикселей в изображении
min_val = np.min(image)
max_val = np.max(image)

# Преобразуем изображение с использованием линейного растяжения контраста
stretched_image = ((image - min_val) * (255 / (max_val - min_val))).astype(np.uint8)

# Сохраним результат
output_path = r'C:\Users\dimab\OneDrive\Desktop\results\image03.jpg'
cv2.imwrite(output_path, stretched_image)


