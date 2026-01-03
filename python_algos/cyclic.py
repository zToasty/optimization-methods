import math
import numpy as np


FUNC_CALLS = 0

def func(x):
    global FUNC_CALLS
    FUNC_CALLS += 1
    return x[0]**2 + 4*x[1]**2 + math.exp(x[0]) + math.exp(x[1])


def gold(f, a, b, epsilon=1e-4, max_iter=100):
    phi = (3 - math.sqrt(5)) / 2
    f_calls = 0

    x1 = a + phi * (b - a)
    x2 = b - phi * (b - a)

    f1 = f(x1); f_calls += 1
    f2 = f(x2); f_calls += 1

    iters = 0
    while abs(b - a) > epsilon and iters < max_iter:
        iters += 1
        if f1 < f2:
            b = x2
            x2 = x1
            f2 = f1
            x1 = a + phi * (b - a)
            f1 = f(x1); f_calls += 1
        else:
            a = x1
            x1 = x2
            f1 = f2
            x2 = b - phi * (b - a)
            f2 = f(x2); f_calls += 1

    x_min = (a + b) / 2
    f_min = f(x_min); f_calls += 1

    return x_min, f_min, f_calls

def find_alpha_interval(f, x, e_j, delta=1, k=1):
    # Начальные точки
    f0 = f(x)
    f_plus = f(x + delta * e_j)
    f_minus = f(x - delta * e_j)

    # Если минимум где-то между [-δ, δ]
    if f0 <= f_plus and f0 <= f_minus:
        return -delta, delta

    # Если функция уменьшается вправо 
    if f_plus < f0 and f_plus <= f_minus:
        a = 0
        b = delta
        step = delta
        while f(x + b * e_j) < f(x + a * e_j):
            a = b
            b += step
            step = step * k ** delta 
        return (min(a, b), max(a, b))

    # Если функция уменьшается влево
    if f_minus < f0 and f_minus <= f_plus:
        b = 0
        a = -delta
        step = -delta
        while f(x + a * e_j) < f(x + b * e_j):
            b = a
            a += step
            step *= 2
        return (min(a, b), max(a, b))

    # На случай если ничего не подошло
    return -delta, delta


def coordinate_descent(f, x0, epsilon=1e-3, max_iter=1000):
    global FUNC_CALLS
    FUNC_CALLS = 0

    x = np.array(x0, dtype=float)
    n = len(x)
    iteration = 0

    while iteration < max_iter:
        iteration += 1
        x_prev = x.copy()

        for j in range(n):
            e_j = np.zeros(n)
            e_j[j] = 1.0

            # Поиск интервала для α по направлению e_j
            a, b = find_alpha_interval(f, x, e_j)

            # === Функция вдоль направления e_j ===
            phi = lambda alpha: f(x + alpha * e_j)

            # === Поиск оптимального α методом золотого сечения ===
            alpha_star, _, _ = gold(phi, a, b, epsilon=1e-4)

            # === Обновление точки ===
            x = x + alpha_star * e_j

        # === Критерий остановки ===
        if abs(f(x) - f(x_prev)) < epsilon:
            print("\nКритерий остановки достигнут")
            print(f"x* = {x}, f* = {f(x):.6f}")
            print(f"Количество обращений к функции: {FUNC_CALLS}")
            return x, f(x), FUNC_CALLS

        print(f"Итерация {iteration}: x={x}, f(x)={f(x):.6f}")

    print("\nДостигнут лимит итераций.")
    print(f"x* = {x}, f* = {f(x):.6f}")
    print(f"Количество обращений к функции: {FUNC_CALLS}")
    return x, f(x), FUNC_CALLS



if __name__ == "__main__":
    x_opt, f_opt, calls = coordinate_descent(func, x0=(1, 1), epsilon=1e-3)
    print("\nРЕЗУЛЬТАТ:")
    print(f"x* = {x_opt}")
    print(f"f* = {f_opt}")
    print(f"Количество обращений к функции: {calls}")
