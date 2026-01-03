import math
import numpy as np


# Целевая функция
def func(x, y):
    return x**2 + 4*y**2 + math.exp(x) + math.exp(y)


def random_search(
    f,
    x0=(1.0, 1.0),
    alpha=1.0,
    epsilon=1e-3,
    gamma=2.0,
    N=100,
    max_iter=1000
):
    """
    Алгоритм случайного поиска (методы оптимизации)
    """
    x0 = np.array(x0, dtype=np.float64)
    x_best = x0.copy()
    f_best = f(x_best[0], x_best[1])
    func_calls = 1
    iteration = 0

    print("=== Алгоритм случайного поиска ===")
    print(f"Начальная точка: x0 = {x0}, f0 = {f_best:.6f}")
    print(f"Параметры: α = {alpha}, γ = {gamma}, ε = {epsilon}, N = {N}\n")

    while iteration < max_iter:
        iteration += 1
        j = 0

        while j < N:
            j += 1

            # Шаг 2: генерируем случайный вектор ξ
            ksi = np.random.randn(len(x0))  # нормальное распределение
            ksi = ksi / np.linalg.norm(ksi)  # нормируем

            # Шаг 3: создаём новую точку
            x_new = x_best + alpha * ksi
            f_new = f(x_new[0], x_new[1])
            func_calls += 1

            # Проверка улучшения
            if f_new < f_best:
                x_best = x_new
                f_best = f_new
                # Если улучшение найдено — продолжаем с той же α
                print(f"Итерация {iteration}.{j}: улучшение f={f_best:.6f}, x={x_best}")
                continue  # возврат к шагу 3

        # Шаг 5: проверка условия остановки
        if alpha < epsilon:
            print("\nКритерий остановки достигнут:")
            print(f"x* = {x_best}, f* = {f_best:.6f}")
            print(f"Количество обращений к функции: {func_calls}")
            return x_best, f_best, func_calls
        else:
            alpha = alpha / gamma
            print(f"\nПонижаем α -> {alpha:.6f}, продолжаем поиск...\n")

    print("\nДостигнут лимит итераций.")
    print(f"x* = {x_best}, f* = {f_best:.6f}")
    print(f"Количество обращений к функции: {func_calls}")
    return x_best, f_best, func_calls


if __name__ == "__main__":
    x_opt, f_opt, calls = random_search(func, x0=(1.0, 1.0), alpha=1.0, epsilon=1e-3, gamma=2.0, N=100)
    print("\nРЕЗУЛЬТАТ:")
    print(f"x* = {x_opt}")
    print(f"f* = {f_opt}")
    print(f"Количество обращений к функции: {calls}")
