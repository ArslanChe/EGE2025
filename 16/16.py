# Порядок
# 1) Пытаемся с помощью @lru_cache(maxsize=None)
# 2) Если ошибка глубины рекурсии -> setrecursionlimit(100000)
# 3) Пытаемся умом оптимизировать

from functools import *
from sys import setrecursionlimit

setrecursionlimit(10000)
# № 14337 (Уровень: Сложный) Решается умом
# функция f не пройдет по глубине рекурсии
# def f(n):
#     if n == 1:
#         return 1
#     return 2*n * f(n - 1)
# print(f(57693))
# Нужно переписать рекурсию на цикл
# def f_1(n):
#     s = 1
#     for i in range(2, n+1):
#         s += 2*i
#     return s
# print(sum(list(map(int,str(f(57693)))))**2)


# № 19882 (Уровень: Базовый) Та же самая задача только с меньшим параметром

# def f(n):
#     if n < 4:
#         return 1
#     return f(n-1) +2*n
# print(f(2025))

# № 19707 (Уровень: Средний)
# def f(n):
#     if n < 3:
#         return 4*n
#     if n >= 3 and n % 2 != 0:
#         return 2*n
#     return 5* f(n - 2)+n*n
# c = 0
# for _ in range(1000):
#     tmp = f(_)
#     if len(str(tmp)) == 3 and tmp % 2 == 0:
#         c += 1
# print(c)

