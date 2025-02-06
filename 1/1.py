from itertools import *

s1 = "1356 26 314 436 51 6124" # Связи в цифрах
s2 = "AB BACE CBD DCE EBDF FE" # Связи в буквах

s2 = {x[0]: frozenset(x[1:]) for x in s2.split()}
for p in permutations("ABCDEF"): # Все буквы
    s3 = s1
    for x, y in zip('123456', p): # Все цифры
        s3 = s3.replace(x, y)
    s3 = {x[0]: frozenset(x[1:]) for x in s3.split()}
    if s2 == s3:
        print('1 2 3 4 5 6')
        print(*p)
