import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter


initial_data_path = r"C:\Users\dimab\OneDrive\Desktop\np3\start.dat"  
u = np.loadtxt(initial_data_path)


size = len(u)


A = np.eye(size) - np.roll(np.eye(size), shift=-1, axis=1)


steps = 255

results = [u.copy()]


for _ in range(steps):
    u = u - 0.5 * A @ u
    results.append(u.copy())


results = np.array(results)


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


anim = FuncAnimation(fig, update, frames=steps + 1, interval=50, blit=True)

output_path = "C:/Users/dimab/OneDrive/Desktop/np3/process_evolution.gif"
anim.save(output_path, writer=PillowWriter(fps=20))



plt.show()


