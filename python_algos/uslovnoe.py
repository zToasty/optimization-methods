import numpy as np

# --- Целевая функция и градиент (в пространстве шара) ---
def g_func(point):
    u, v, w = point
    return 16**u + 27**v + 16**w

def grad_g(point):
    u, v, w = point
    return np.array([
        16**u * np.log(16),
        27**v * np.log(27),
        16**w * np.log(16)
    ])

# --- Метод условного градиента с дроблением шага ---
def solve_conditional_gradient_linesearch(tol):
    # Шаг 0: Начальная точка (u, v, w)
    curr = np.array([0.5, 1.0/3.0, 0.25])
    max_iter = 5000

    print(f"Start algorithm with tol={tol}")

    for i in range(max_iter):
        f_curr = g_func(curr)
        
        grad = grad_g(curr)
        grad_norm = np.linalg.norm(grad)
        
        if grad_norm == 0:
            break
        s = -grad / grad_norm
        
        gap = np.dot(grad, curr - s)
        if gap < tol:
            curr = s # Можно остановиться
            break

        alpha = 0.1
        direction = s - curr
        
        while True:
            next_candidate = curr + alpha * direction
            f_next = g_func(next_candidate)
            
            # Если функция уменьшилась - принимаем шаг
            # (Добавлена защита alpha > 1e-10 чтобы не уйти в бесконечный цикл)
            if f_next < f_curr or alpha < 1e-10:
                break
            
            # Иначе делим пополам
            alpha /= 2.0
            
        # Обновляем точку
        curr = next_candidate
        
        # Проверка на очень маленькие изменения (дополнительная защита)
        if alpha < 1e-10:
            break

    # Обратное преобразование координат для ответа
    x, y, z = curr[0]*2, curr[1]*3, curr[2]*4
    f_val = 4**x + 3**y + 2**z
    
    print(f"Tol: {tol:<7} | Iter: {i:<5} | x: {x:.6f}, y: {y:.6f}, z: {z:.6f} | f(x): {f_val:.6f}")

# --- Запуск ---
print("-" * 75)
solve_conditional_gradient_linesearch(1e-3)
solve_conditional_gradient_linesearch(1e-4)
print("-" * 75)