import numpy as np
import matplotlib.pyplot as plt

# Загрузим данные из файла
data_path = r'C:\Users\dimab\OneDrive\Desktop\signals\signal03.dat'
data = np.loadtxt(data_path)

# Зададим размер окна для скользящего среднего
window_size = 10

# Создадим массив для хранения фильтрованных данных
filtered_data = np.copy(data)

# Применим фильтр скользящего среднего
for i in range(len(data)):
    # Рассчитываем среднее от 0 до i, если i < window_size
    if i < window_size:
        filtered_data[i] = np.mean(data[:i+1])
    else:
        filtered_data[i] = np.mean(data[i-window_size+1:i+1])

# Визуализируем исходные и фильтрованные данные
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.plot(data, label='Raw Signal')
plt.title("Сырой сигнал")
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(filtered_data, label='Filtered Signal', color='orange')
plt.title("После фильтра")
plt.legend()

# Сохраним график в файл
output_path = r'C:\Users\dimab\OneDrive\Desktop\results2\graph03'
plt.savefig(output_path)

plt.show()
