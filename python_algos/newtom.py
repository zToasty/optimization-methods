import math

def func(x):
    return math.exp(x) + x ** 4

def f_prime(x):
    return math.exp(x) + 4 * x ** 3

def f_double_prime(x):
    return math.exp(x) + 12 * x ** 2

def newton_method_for_min(func, f_prime, f_double_prime, x0, eps, max_iter=100):
    x = x0
    cnt = 0

    for i in range(max_iter):
        fp = f_prime(x)
        fpp = f_double_prime(x)

        if abs(fp) < eps:
            break

        x_new = x - (fp/fpp)
        cnt += 1

        if abs(x_new - x) < 2 * eps:
            x = x_new
            break

        x = x_new

    x_min = x
    f_min = func(x_min)
    return x_min, f_min, cnt 



x0 = 0
eps = 1e-4

try:
    x_min, f_min, calls = newton_method_for_min(func, f_prime, f_double_prime, x0, eps)
    print(f"x_min = {x_min:.6f}")
    print(f"f_min = {f_min:.6f}")
    print(f"Количество вызовов: {calls}")
    print(f"f'(x_min) = {f_prime(x_min):.6f}")
    print(f"f''(x_min) = {f_double_prime(x_min):.6f}")
except ValueError as e:
    print(e)