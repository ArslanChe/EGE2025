# # Для перевода 10 -> 2, 8, 16 используем f-строки
# a = 1234
# print(f'{a:b}')
# print(f'{a:o}')
# print(f'{a:x}')
# # Для перевода из N -> 10 используем int(str(N),10)
# print(int(str(100),2))
# # Для перевода из 10 -> K
# def convert(n,k):
#     s = ''
#     while n > 0:
#         s = str(n%k) + s
#         n = n // k
#     return s
# print(convert(1234,2)) # Проверим на двоичной


# def f(n):
#     s = f'{n:b}'
#     s = s + s[-1]
#     if s.count('1') % 2 == 0:
#         s=  s + '0'
#     else:
#         s= s+ '1'
#     if s.count('1') % 2 == 0:
#         s = s + '0'
#     else:
#         s= s + '1'
#     return int(s,2)
# ans = []
# for i in range(1,100000):
#     if f(i)> 105:
#         ans.append((f(i), i))
# print(min(ans))
# print(bin(111))

def t(n):
    ans = ''
    while n>0:
        last = n % 3
        n //= 3
        ans = str(last)+  ans
    return ans
def task(n):
    tmp = t(n)
    if n % 3 == 0:
        return int(tmp+ tmp[-2:],3)
    else:
        return int(tmp + t(n%3*3),3)
for i in range(3,10000):
    if task(i) <=150:
        print(i)