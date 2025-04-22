#19878
# Чтение файла
# with open("9.txt") as f:
#     c = 0
#     # Чтение строки
#     for line in f:
#         s = list(map(int,line.strip().split()))
#
#         # Обработка строки
#         if len(set(s)) == 5:
#             d = {}
#             for i in s:
#                 d[i] = d.get(i,0) + 1
#             s1 = 0
#             s3 = 0
#             for j in d:
#                 if d[j] == 3:
#                     s3 =j
#                 if d[j] != 3:
#                     s1+= j
#             if s1/4 <= s3:
#                 c+= 1
#     print(c)

with open("9.txt") as f:
    c = 0
    for line in f:
        s = list(map(int,line.split()))
        if all(s[i] > s[i+1] for i in range(len(s)-1)) and (max(s)+min(s))/2 > (sum(s) - max(s)-min(s))/5:
            print(sum(s))
            break
