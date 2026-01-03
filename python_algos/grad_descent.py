import math
import numpy as np


# Целевая функция
def func(x, y):
    return x**2 + 4*y**2 + math.exp(x) + math.exp(y)


# Градиент функции
def grad_func(x, y):
    df_dx = 2 * x + math.exp(x)
    df_dy = 8 * y + math.exp(y)
    return np.array([df_dx, df_dy], dtype=np.float64)


def gradient_descent(
    f,
    grad_f,
    x0=(1.0, 1.0),
    alpha=0.1,
    epsilon=1e-3,
    max_iter=100
):
    """
    Алгоритм градиентного спуска (методы оптимизации)
    """
    x = np.array(x0, dtype=np.float64)
    func_calls = 0
    grad_calls = 0
    iteration = 0

    f_current = f(x[0], x[1])
    func_calls += 1
    f_best = f_current

    print("=== Алгоритм градиентного спуска ===")
    print(f"Начальная точка: x0 = {x}, f(x0) = {f_current:.6f}")
    print(f"Параметры: α = {alpha}, ε = {epsilon}\n")

    while iteration < max_iter:
        iteration += 1

        # Шаг 1: вычисляем градиент
        grad = grad_f(x[0], x[1])
        grad_calls += 1
        norm_grad = np.linalg.norm(grad)

        if norm_grad <= epsilon:
            print("\nКритерий остановки достигнут:")
            print(f"x* = {x}, f* = {f_current:.6f}")
            print(f"Количество обращений к функции: {func_calls}")
            print(f"Количество вычислений градиента: {grad_calls}")
            return x, f_current, func_calls, grad_calls

        # Делаем шаг против градиента
        x_new = x - alpha * grad
        f_new = f(x_new[0], x_new[1])
        func_calls += 1

        # Шаг 2: проверяем улучшение
        if f_new > f_current:
            alpha = alpha / 2.0
            print(f"Итерация {iteration}: ухудшение f={f_new:.6f}, уменьшаем α -> {alpha:.6f}")
            continue  # возвращаемся к шагу 1 без обновления x
        else:
            x = x_new
            f_current = f_new
            f_best = min(f_best, f_current)
            print(f"Итерация {iteration}: f={f_current:.6f}, x={x}, ||grad||={norm_grad:.6f}")

    print("\nДостигнут лимит итераций.")
    print(f"x* = {x}, f* = {f_current:.6f}")
    print(f"Количество обращений к функции: {func_calls}")
    print(f"Количество вычислений градиента: {grad_calls}")
    return x, f_current, func_calls, grad_calls


if __name__ == "__main__":
    x_opt, f_opt, calls_f, calls_g = gradient_descent(
        func, grad_func, x0=(1.0, 1.0), alpha=0.1, epsilon=1e-3
    )

    print("\nРЕЗУЛЬТАТ:")
    print(f"x* = {x_opt}")
    print(f"f* = {f_opt}")
    print(f"Количество обращений к функции: {calls_f}")
    print(f"Количество вычислений градиента: {calls_g}")
