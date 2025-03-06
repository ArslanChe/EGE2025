#Код для сопоставления графов

from itertools import *

s1 = "126 2147 3456 4236 537 6134 725" # Связи в цифрах
s2 = "ABDG BACG CBD DACE EDF FEG GABF" # Связи в буквах

s2 = {x[0]: frozenset(x[1:]) for x in s2.split()}
for p in permutations("ABCDEFG"): # Все буквы
    s3 = s1
    for x, y in zip('1234567', p): # Все цифры
        s3 = s3.replace(x, y)
    s3 = {x[0]: frozenset(x[1:]) for x in s3.split()}
    if s2 == s3:
        print('1 2 3 4 5 6 7')
        print(*p)
