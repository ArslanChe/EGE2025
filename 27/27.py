from math import *
# №18678
data = [tuple(map(float, f.split())) for f in open('27A_18678.txt')]
# Аналитическое рабзиение на кластеры
# Отбор аномалий происходит с помощью добавление условий выбора кластера
clusters = [[],[]]
for p in data:
    if (p[0] < 1 and p[1] >4) or (p[0] >6.5 and p[1]>2.5):
        continue
    elif  p[1] < 2: # Условие (строится по визуализации в экселе)
        clusters[0].append(p)
    else:
        clusters[1].append(p)
for i in clusters:
    print(len(i))

print()
# Программное разбиение на кластеры
# Отбор аномалий происходит с помощью изменения дистанции для выбора кластера
clusters = []
while data:
    clusters.append([data.pop()])
    for p1 in clusters[-1]:
        for p2 in data[:]:
            if dist(p1, p2) <1 :
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