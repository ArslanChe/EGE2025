from math import *

data = [tuple(map(int, f.split())) for f in open('27_A_18884.txt')]
# Аналитическое рабзиение на кластеры
# Отбор аномалий происходит с помощью добавление условий выбора кластера
clusters = [[],[]]
for p in data:
    if p[0] > 40: # Условие (строится по визуализации в экселе)
        clusters[0].append(p)
    else:
        clusters[1].append(p[1])
for i in clusters:
    print(len(i))


# Программное разбиение на кластеры
# Отбор аномалий происходит с помощью изменения дистанции для выбора кластера
clusters = []
while data:
    clusters.append([data.pop()])
    for p1 in clusters[-1]:
        for p2 in data[:]:
            if dist(p1, p2) <10:
                clusters[-1].append(p2)
                data.remove(p2)
for i in clusters:
    print(len(i))





#
# def operate(cluster):
#     ans = (1e10, ())
#     for p in cluster:
#         dl = sum([dist(p, p1) for p1 in cluster])
#         if dl< ans[0]:
#             ans = (dl, p)
#     return ans
# for i in clusters:
#     print(operate(i))