import numpy as np

# 1. Новая целевая функция g(u, v, w)
def g_func(u, v, w):
    return 16**u + 27**v + 16**w

# 2. Градиент новой функции
def grad_g(point):
    u, v, w = point
    return np.array([
        16**u * np.log(16),
        27**v * np.log(27),
        16**w * np.log(16)
    ])


def solve_projection(tol):
    curr = np.array([0.5, 1.0/3.0, 0.25])
    lr = 0.1
    max_iter = 5000

    for i in range(max_iter):
        u, v, w = curr
        
        # Градиент
        grad = np.array([
            16**u * np.log(16),
            27**v * np.log(27),
            16**w * np.log(16)
        ])
        
        next_p = curr - lr * grad
        norm = np.linalg.norm(next_p)
        if norm > 1:
            next_p = next_p / norm  # Проекция на границу шара
            
        # Проверка остановки
        if np.linalg.norm(next_p - curr) < tol:
            curr = next_p
            break
        curr = next_p

    # Обратное преобразование
    x, y, z = curr[0]*2, curr[1]*3, curr[2]*4
    f_val = 4**x + 3**y + 2**z
    
    print(f"Tol: {tol:<7} | Iter: {i:<4} | x: {x:.6f}, y: {y:.6f}, z: {z:.6f} | f(x): {f_val:.6f}")

print("-" * 75)
solve_projection(1e-3)
solve_projection(1e-4)
print("-" * 75)