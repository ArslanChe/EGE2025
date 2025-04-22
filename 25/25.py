# from math import *
# def div(n):
#     divs = set()
#     d = 2
#     while d * d <= n:
#         if n % d == 0:
#             divs.add(d)
#             divs.add(n//d)
#         d += 1
#
#     return list(sorted(divs))
#
# c = 0
# n =200_000_001
# while c != 5:
#     if 0< prod(div(n)[:5]) < n :
#         c += 1
#         print(prod(div(n)[:5]))
#     n+= 1

from fnmatch import *
for i in range(0,10**10,7993):
    if fnmatch(str(i),'4*4736*1'):
        print(i, i//7993)