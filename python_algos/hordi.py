import math

call_count = 0

def func(x):
    return math.exp(x) + x ** 4

# def f_prime(x):
#     return math.exp(x) + 4 * x ** 3

def f_prime(x):
    global call_count
    call_count += 1
    print(f"Вызов f_prime({x:.6f}), вызов №{call_count}")
    return math.exp(x) + 4 * x ** 3

def chord_method(a, b, func, eps):
    cnt = 0
    df_cnt = 0

    fa_prime = f_prime(a)
    df_cnt += 1

    if fa_prime >= 0:
        f_min = func(a)
        x_min = a
        cnt += 1
        return x_min, f_min, cnt, fa_prime, df_cnt  

    fb_prime = f_prime(b)
    df_cnt += 1

    if fb_prime <= 0:
        f_min = func(b)
        x_min = b
        cnt += 1
        return x_min, f_min, cnt, fb_prime, df_cnt 

    while b - a > eps:
        c = (a + b) / 2
        df = f_prime(c)
        df_cnt += 1

        if abs(df) < eps:
            x_min = c
            f_min = func(c)
            cnt += 1
            break

        if df < 0:
            a = c
        else:
            b = c

    return x_min, f_min, cnt, f_prime(x_min), df_cnt
results = chord_method(-1, 1, func, 1e-4)
print(f'Results 4: x_min =  {results[0]}; f_min = {results[1]}; df_min {results[3]}; cnt = {results[2]}; df_cnt = {results[4]}')
results = chord_method(-1, 1, func, 1e-3)
print(f'Results 3: x_min =  {results[0]}; f_min = {results[1]}; df_min {results[3]}; cnt = {results[2]}; df_cnt = {results[4]}')