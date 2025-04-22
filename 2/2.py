# Использовать мозг для сопоставления с данной таблицей
# print('x y z w')
# for x in 0, 1:
#     for y in 0, 1:
#         for z in 0, 1:
#             for w in 0, 1:
#                 if (((not x or y) and not w) or (not (z and not(y and w)))):
#                     print(x, y, z, w)
#
# from itertools import product, permutations
# # Максимально кодом
# def f(x, y, z, w):
#     return not (((not x or y) and not w) or (not (z and not(y and w))))
#
# # x1, x2, ... x => меняем repeat = число пропусков
# for x1, x2,x3,x4,x5,x6,x7,x8 in product([0, 1], repeat=8):
#     # Вся исходная таблица
#     tmp = (
#         (0, x1, x2, 1, 0),
#         (x4, 1, x5, x6, 0),
#         (1, 0, x7, x8, 0)
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
print("x y z w")
for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                f = (not(x<=y)) or (z==w) or z
                if not f:
                    print(x,y,z,w, f)
print((not(0<=1)) or (0==1) or 0)
# Ответ: zyxw