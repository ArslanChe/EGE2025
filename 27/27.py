from math import *
# №18678
# data = [tuple(map(float, f.split())) for f in open('27B.txt')]
# Аналитическое рабзиение на кластеры
# Отбор аномалий происходит с помощью добавление условий выбора кластера
# clusters = [[],[]]
# for p in data:
#     if (p[0] < 1 and p[1] >4) or (p[0] >6.5 and p[1]>2.5):
#         continue
#     elif  p[1] < 2: # Условие (строится по визуализации в экселе)
#         clusters[0].append(p)
#     else:
#         clusters[1].append(p)
# for i in clusters:
#     print(len(i))

# print()
# Программное разбиение на кластеры
# Отбор аномалий происходит с помощью изменения дистанции для выбора кластера
# clusters = []
# while data:
#     clusters.append([data.pop()])
#     for p1 in clusters[-1]:
#         for p2 in data[:]:
#             if dist(p1, p2) <2 :
#                 clusters[-1].append(p2)
#                 data.remove(p2)
# for i in clusters:
#     print(len(i))



# from itertools import *
#
# #
# def operate(cluster):
#     ans = (1e10, ())
#     for p in cluster:
#         dl = sum([dist(p, p1) for p1 in cluster])
#         if dl< ans[0]:
#             ans = (dl, p)
#     return ans
# ans = []
# for i in clusters:
#     ans.append(operate(i)[1])
# mn = float('inf')
# for x in permutations(ans, 2):
#     mn = min(mn, dist(x[0], x[1]))
# print(mn*10000)




#
# # №19257
# data = [tuple(map(float, f.split())) for f in open('27B.txt')]
# # Аналитическое рабзиение на кластеры
# # Отбор аномалий происходит с помощью добавление условий выбора кластера
# clusters = [[],[],[]]
# for p in data:
#     if p[0]< 0:
#         clusters[0].append(p)
#     elif  p[1]<8 and p[1]>0:
#         clusters[1].append(p)
#     else:
#         clusters[2].append(p)
# for c in clusters:
#     print(len(c))
# def operate(cluster):
#     ans = (1e10, ())
#     for p in cluster:
#         sm = sum([dist(p, p1) for p1 in cluster])
#         if sm < ans[0]:
#             ans = (sm, p)
#     return ans
# ansx = 0
# ansy = 0
# for i in clusters:
#     print(operate(i))
#     ansx+= operate(i)[1][0]
#     ansy+= operate(i)[1][1]
#
# print(ansx*10000/3)
# print(ansy*10000/3)



points = [tuple(map(float, f.split())) for f in open('27A.txt')]
cl1 = []
cl2 = []
for p in points:
    if p[1] > -2:
        cl1.append(p)
    else:
        cl2.append(p)
def operate(cluster):
    ans = (1e10, ())
    for p in cluster:
        dl = sum([dist(p, p1) for p1 in cluster])
        if dl< ans[0]:
            ans = (dl, p)
    return ans
c1 =operate(cl1)
c2 = operate(cl2)
px =(c1[1][0]+c2[1][0])/2
py = (c1[1][1]+c2[1][1])/2
print(px*10000, py*10000)