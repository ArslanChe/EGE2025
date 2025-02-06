# Для перевода 10 -> 2, 8.md, 16 используем
a = 1234
print(f'{a:b}')
print(f'{a:o}')
print(f'{a:x}')
# Для перевода из N -> 10 используем int(str(N),10)
print(int(str(100),2))
# Для перевода из 10 -> K
def convert(n,k):
    s = ''
    while n > 0:
        s = str(n%k) + s
        n = n // k
    return s
print(convert(1234,2)) # Проверим на двоичной

