# Порядок
# 0) Переписываем функцию из условия


# 1) Пытаемся с помощью @lru_cache(maxsize=None)
    #1.1) Предпросчитываем функцию for _ in range(0,1000): f(_)
    #1.2) Получаем ответ
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

# def f(n):
#     if n > 400:
#         return n**n
#     return n+6+f(n+12)
# print(f(72)-f(108))


#5154
# def f(n):
#     if n > 100_000:
#         return n
#     return f(n+1)+5*n+2
# print(f(3)- f(7))
# @lru_cache(maxsize=None)
# def f(n):
#     if n == 0: return 0
#     if n >0 and n %2 == 0:
#         return f(n//10) + n%10
#     return f(n//10)
# c = 0
# for i in range(10**7,6*10**7+1):
#     if f(i) == 0:
#         c += 1
# print(c)
@lru_cache(maxsize=None)
def f(n):
    if n < 20:
        return n
    return (n-6)*f(n-7)
for _ in range(50000):
    f(_)
print((f(47872)-290*f(47865))/f(47858))