import math


def gold(f, a, b, epsilon, max_iter=100):
    phi = (math.sqrt(5) - 1) / 2

    x1 = b - phi * (b - a)
    x2 = a + b - x1

    f1 = f(x1)
    f2 = f(x2)

    iters = 2

    while abs(b - a) > epsilon:
        iters += 1
        
        if f1 < f2:
            b = x2
            x2 = x1
            f2 = f1
            x1 = a + b - x2
            f1 = f(x1)

        else:
            a = x1
            x1 = x2
            f1 = f2
            x2 = a + b - x1
            f2 = f(x2)

    x_min = (a+b)/2
    f_min = f(x_min)

    return x_min, f_min, iters


def func(x):
    return x**2 + math.exp(x)

for epsilon in [10**-3, 10**-4]:
    x_min, f_min, iters = gold(func, -1, 1, epsilon)
    print(f"epsilon = {epsilon:.0e}: x_min = {x_min:.8f}, f_min = {f_min:.8f}, вызовов = {iters}")

