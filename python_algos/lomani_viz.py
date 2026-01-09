import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# --- НАСТРОЙКИ ---
def func(x):
    return np.sin(x) + np.sin(2.3 * x) * 0.5 + (x - 2)**2 * 0.05

A, B = -2, 8
L = 3.5 
FRAMES = 20

# --- ЛОГИКА ---
x_grid = np.linspace(A, B, 1000)
y_true = func(x_grid)
measured_points = [A, B]
measured_values = [func(A), func(B)]

def calculate_minorant(x_grid, points, values, L):
    cones = []
    for xi, yi in zip(points, values):
        cone = yi - L * np.abs(x_grid - xi)
        cones.append(cone)
    return np.max(cones, axis=0)

def find_next_point(points, values, L):
    sorted_indices = np.argsort(points)
    xs = np.array(points)[sorted_indices]
    ys = np.array(values)[sorted_indices]
    min_p_val = float('inf')
    next_x = A
    for i in range(len(xs) - 1):
        x1, y1 = xs[i], ys[i]
        x2, y2 = xs[i+1], ys[i+1]
        x_tip = 0.5 * (x1 + x2) + (y1 - y2) / (2 * L)
        p_tip = 0.5 * (y1 + y2) - L * (x2 - x1) / 2
        if p_tip < min_p_val:
            min_p_val = p_tip
            next_x = x_tip
    return next_x

# --- ВИЗУАЛИЗАЦИЯ ---
fig, ax = plt.subplots(figsize=(8, 5)) # Чуть меньше размер для GIF
ax.set_xlim(A, B)
ax.set_ylim(np.min(y_true) - 3, np.max(y_true) + 1)

line_true, = ax.plot(x_grid, y_true, 'b-', linewidth=2, label='f(x)')
line_minorant, = ax.plot([], [], 'r--', linewidth=1.5, label='Миноранта')
scat_points = ax.scatter([], [], c='green', s=60, zorder=5)
title = ax.set_title('')
ax.legend(loc='upper right')
ax.grid(True)

def update(frame):
    if frame > 0:
        new_x = find_next_point(measured_points, measured_values, L)
        new_y = func(new_x)
        measured_points.append(new_x)
        measured_values.append(new_y)
        
    current_minorant = calculate_minorant(x_grid, measured_points, measured_values, L)
    
    line_minorant.set_data(x_grid, current_minorant)
    scat_points.set_offsets(np.column_stack((measured_points, measured_values)))
    
    best_idx = np.argmin(measured_values)
    title.set_text(f'Шаг {frame}. Рекорд: {measured_values[best_idx]:.3f}')
    return line_minorant, scat_points, title

# Создаем анимацию
ani = animation.FuncAnimation(fig, update, frames=FRAMES, interval=500, repeat=False)

# --- СОХРАНЕНИЕ ---
print("Генерирую GIF... Подожди пару секунд.")
# writer='pillow' использует стандартную библиотеку Python, не нужен ffmpeg
ani.save('lomani.gif', writer='pillow', fps=2) 
print("Готово! Файл lomani.gif сохранен.")