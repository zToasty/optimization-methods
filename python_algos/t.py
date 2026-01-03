import math
import numpy as np
import matplotlib.pyplot as plt

def func(x):
    return math.cos(x) + (10*x - x**2)/50

def method_of_broken_lines(epsilon=1e-3, max_iter=100):
    """
    Метод ломаных для минимизации функции
    """
    L = 0.2  # Константа Липшица
    
    # Начальный интервал
    a, b = 0, 10
    fa, fb = func(a), func(b)
    
    # Шаг 0: Строим первую ломанную
    x1 = (a + b)/2 + (fa - fb)/(2*L)
    phi1 = (fa + fb)/2 - L*(b - a)/2
    
    print("ШАГ 0:")
    print(f"x1 = {x1:.6f}")
    print(f"φ1 = {phi1:.6f}")
    print(f"f(x1) = {func(x1):.6f}")
    
    # Сохраняем точки ломанной
    points = [x1]
    phi_values = [phi1]
    f_values = [func(x1)]
    
    for iteration in range(1, max_iter + 1):
        print(f"\nШАГ {iteration}:")
        
        # НАХОДИМ i: φ_i = min_j φ_j
        min_phi_index = np.argmin(phi_values)
        x_min = points[min_phi_index]
        phi_min = phi_values[min_phi_index]
        f_min = f_values[min_phi_index]
        
        print(f"min φ_j: x{min_phi_index+1} = {x_min:.6f}")
        print(f"φ{min_phi_index+1} = {phi_min:.6f}")
        print(f"f(x{min_phi_index+1}) = {f_min:.6f}")
        
        # Проверка условия остановки
        if abs(f_min - phi_min) < epsilon:
            print(f"Найден минимум: x = {x_min:.6f}, f(x) = {f_min:.6f}")
            return x_min, f_min, iteration
        
        # Добавляем новую точку в ломанную
        # (здесь нужно уточнить стратегию добавления новых точек)
        x_new = (a + b)/2  # Простой пример - середина интервала
        phi_new = func(x_new) - L * abs(x_new - x_min)  # Нижняя оценка
        f_new = func(x_new)
        
        points.append(x_new)
        phi_values.append(phi_new)
        f_values.append(f_new)
        
        print(f"Добавлена точка x{len(points)} = {x_new:.6f}")
        print(f"φ{len(points)} = {phi_new:.6f}")
    
    print("Достигнут максимум итераций")
    return points[-1], f_values[-1], max_iter

# Запуск метода
if __name__ == "__main__":
    print("МЕТОД ЛОМАННЫХ ДЛЯ МИНИМИЗАЦИИ")
    print("Функция: cos(x) + (10x - x²)/50")
    print("Интервал: [0, 10], L = 0.2")
    print("=" * 50)
    
    x_opt, f_opt, iters = method_of_broken_lines()
    
    print(f"\nРезультат:")
    print(f"x_опт = {x_opt:.6f}")
    print(f"f(x_опт) = {f_opt:.6f}")
    print(f"Итераций: {iters}")