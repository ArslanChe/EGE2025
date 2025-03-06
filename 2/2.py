# Использовать мозг для сопоставления с данной таблицей
# print('x y z w')
# task = "Логическое выражение"
# for x in 0, 1:
#     for y in 0, 1:
#         for z in 0, 1:
#             for w in 0, 1:
#                 if task:
#                     print(x, y, z, w)

# from itertools import product, permutations
# # Максимально кодом
# def f(x, y, z, w):
#     return ((w <= (y == z)) and (y == (z <= x)))
#
# # x1, x2, ... x => меняем repeat = число пропусков
# for x1, x2 in product([0, 1], repeat=2):
#     # Вся исходная таблица
#     tmp = (
#         (x1, 0, 0, 0, 1),
#         (0, x2, 1, 1, 1),
#         (0, 0, 0, 1, 1)
#     )
#     # Проверяем что строки не пропали
#     if len(tmp) == len(set(tmp)):
#         # Перебираем буквы
#         for p in permutations('xyzw', 4):
#             # Подставляем значения перестановки, сопоставляя буквы, в функцию и проверяем результат
#             if all(f(**dict(zip(p, t))) == t[-1] for t in tmp):
#                 print(*p)
#                 break
# print('x y z w')
# for x in range(0,2):
#     for y in range(0,2):
#         for z in range(0,2):
#             for w in range(0,2):
#                 if not(w <= (x==y))and(z<=x):
#                     print(x,y,z,w)


for x in (0,1):
    for y in (0,1):
        for z in (0,1):
            for w in (0,1):
                if(w== not())