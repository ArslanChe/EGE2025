# 18976
from itertools import  product
# k = 0
# for i in product([i for i in range(20)],repeat = 5):
#     if i[0] != 0 and all(i[j] % 2 != i[j+1] % 2 for j in range(4)) and (i[0]+i[-1]) == 26:
#         k += 1
# print(k)


# 19240
# for i, t in enumerate(product(sorted('ЯНВАРЬ'), repeat = 5)):
#     s = ''.join(t)
#
#     if s[0] != 'Я' and s.count('Ь') <= 1 and s.count('ЯЯ') == 0:
#         print(i + 1)

for i, t in enumerate(product(sorted('МАРИЯ'), repeat=4)):
    s = ''.join(t)
    if s == 'АРИЯ':
        print(i+1)
        break