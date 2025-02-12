# Порядок
# 1) Пытаемся с помощью @lru_cache(maxsize=None)
# 2) Если ошибка глубины рекурсии -> setrecursionlimit(100000)
# 3) Пытаемся умом оптимизировать

import  sys
from functools import lru_cache


@lru_cache(maxsize=None)
def f(s, t):
    # Условие окончания подсчета/запрещенные поля
    if s < t or s == 28 : return 0
    # Условие нужного пути
    if s==t: return 1
    #Условие перехода
    if s % 2==0:
        return f(s//2, t) + f(s-2, t)
    else:
        return f(s-3, t) + f(s-2, t)

print(f(98, 1))
