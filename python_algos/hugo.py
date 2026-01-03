import math
import numpy as np


def func(x, y):
    return x**2 + 4*y**2 + math.exp(x) + math.exp(y)


# AC
def AC(f, x, delta, func_calls):
    n = len(x)
    x_minus = x.copy()

    for j in range(n):
        e_j = np.zeros(n)
        e_j[j] = 1.0

        # Step 1
        f_current = f(x_minus[0], x_minus[1])
        func_calls += 1
        f_plus = f(x_minus[0] + delta[j]*e_j[0], x_minus[1] + delta[j]*e_j[1])
        func_calls += 1

        if f_plus < f_current:
            x_minus = x_minus + delta[j] * e_j
            continue  # go to step 3

        # Step 2
        f_minus = f(x_minus[0] - delta[j]*e_j[0], x_minus[1] - delta[j]*e_j[1])
        func_calls += 1

        if f_minus < f_current:
            x_minus = x_minus - delta[j] * e_j
            # go to step 3

    return x_minus, func_calls



def hooke_jeeves(
    f,
    x0=(1, 1),
    delta=(1, 1),
    epsilon=1e-3,
    gamma=2,
    max_iter=1000
):
    x0 = np.array(x0, dtype=np.float32)
    delta = np.array(delta, dtype=np.float32)
    func_calls = 0
    iteration = 0

    while iteration < max_iter:
        iteration += 1

        x0_minus, func_calls = AC(f, x0, delta, func_calls)

        if np.allclose(x0, x0_minus, atol=1e-12):
            # step 2
            if np.linalg.norm(delta) <= epsilon:
                print("\n Критерий остановки достигнут:")
                print(f"x* = {x0_minus}, f* = {f(x0_minus[0], x0_minus[1]):.6f}")
                print(f"Количество обращений к функции: {func_calls}")
                return x0_minus, f(x0_minus[0], x0_minus[1]), func_calls
            else:
                delta = delta / gamma
                continue  # go to step 1

        # step 3
        x1 = 2 * x0_minus - x0

        # step 4
        x1_minus, func_calls = AC(f, x1, delta, func_calls)
        f_x1_minus = f(x1_minus[0], x1_minus[1])
        f_x0_minus = f(x0_minus[0], x0_minus[1])
        func_calls += 2

        if f_x1_minus < f_x0_minus:
            x0 = x0_minus
            x0_minus = x1_minus
        else:
            x0 = x1_minus

        print(f"Итерация {iteration}: f(x)={f_x0_minus:.6f}, x={x0_minus}, δ={delta}")

    print("\nДостигнут лимит итераций.")
    print(f"x* = {x0_minus}, f* = {f(x0_minus[0], x0_minus[1]):.6f}")
    print(f"Количество обращений к функции: {func_calls}")
    return x0_minus, f(x0_minus[0], x0_minus[1]), func_calls


if __name__ == "__main__":
    x_opt, f_opt, calls = hooke_jeeves(func, x0=(1, 1), delta=(1, 1), epsilon=1e-3)
    print("\nРЕЗУЛЬТАТ:")
    print(f"x* = {x_opt}")
    print(f"f* = {f_opt}")
    print(f"Количество обращений к функции: {calls}")
