import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter


# Загрузка начальных данных
initial_data_path = r"C:\Users\dimab\OneDrive\Desktop\np3\start.dat"  # Укажите путь к вашему файлу
u = np.loadtxt(initial_data_path)

# Размерность данных
size = len(u)

# Создание матрицы A
A = np.eye(size) - np.roll(np.eye(size), shift=-1, axis=1)

# Число шагов
steps = 255

# Сохранение результатов
results = [u.copy()]

# Итеративный процесс
for _ in range(steps):
    u = u - 0.5 * A @ u
    results.append(u.copy())

# Преобразование результатов в массив для визуализации
results = np.array(results)

# Создание анимации
fig, ax = plt.subplots(figsize=(8, 5))
line, = ax.plot(results[0], color='blue')
ax.set_xlim(0, size - 1)
ax.set_ylim(results.min(), results.max())
ax.set_xlabel('x')
ax.set_ylabel('u(x)')
ax.set_title('Эволюция процесса')

def update(frame):
    line.set_ydata(results[frame])
    ax.set_title(f'Эволюция процесса')
    return line,

# Запуск анимации
anim = FuncAnimation(fig, update, frames=steps + 1, interval=50, blit=True)

output_path = "C:/Users/dimab/OneDrive/Desktop/np3/process_evolution.gif"
anim.save(output_path, writer=PillowWriter(fps=20))
print(f"GIF сохранён в {output_path}")

# Отображение анимации
plt.show()


