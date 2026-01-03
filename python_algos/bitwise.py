import math

def my_func(x):
    return math.exp(x) + x**2

def bitwise(a, b, eps):
    cnt = 0
    delta = (b - a) / 4   # начальный шаг

    # начальные точки
    x_vals = [a + i*delta for i in range(5)]
    f_vals = [my_func(x) for x in x_vals]; cnt += 5
    compiled = dict(zip(x_vals, f_vals))
    while_cnt = 1
    while (b - a) > 2*eps:
        while_cnt += 1
        # находим минимум
        min_idx = f_vals.index(min(f_vals))
        x_min, f_min = x_vals[min_idx], f_vals[min_idx]
        
        # сужаем интервал
        if min_idx == 0:  
            a, b = x_vals[0], x_vals[1]
        elif min_idx == len(x_vals)-1:
            a, b = x_vals[-2], x_vals[-1]
        else:
            a, b = x_vals[min_idx-1], x_vals[min_idx+1]
        
        # уменьшаем шаг
        delta = (b - a) / 4

        # новые 5 точек (равномерная сетка)
        x_vals = [a + i*delta for i in range(5)]
        f_vals = []
        for x in x_vals:
            if x not in compiled:
                fx = my_func(x)
                compiled[x] = fx
                cnt += 1
            else:
                fx = compiled[x]
            f_vals.append(fx)
    
    # финальный ответ
    x_ans = (a + b) / 2
    if x_ans not in compiled:
        f_ans = my_func(x_ans); cnt += 1
    else:
        f_ans = compiled[x_ans]
    
    return x_ans, f_ans, cnt, while_cnt

result1 = bitwise(-1, 1, 1e-4)
result2 = bitwise(-1, 1, 1e-3)

print("=" * 80)
print(f"{'Показатель':<20} | {'1e-4':<30} | {'1e-3':<30}")
print("=" * 80)
print(f"{'Точка минимума':<20} | {result1[0]:<30.10f} | {result2[0]:<30.10f}")
print(f"{'Значение функции':<20} | {result1[1]:<30.10f} | {result2[1]:<30.10f}")
print(f"{'Количество вызовов':<20} | {result1[2]:<30} | {result2[2]:<30}")
print(f"{'Количество итераций':<20} | {result1[3]:<30} | {result2[3]:<30}")
print("=" * 80)