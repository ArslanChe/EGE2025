# with open("24_318.txt") as f:
#     s = f.read()
#     for i in range(len(s)):
#         if s[i].isalpha():
#             s = s.replace(s[i], ' ')
#     print(s.split())
# import re
# mx = 0
# with open("24_17641.txt") as f:
#     s = f.read()
#     num = r'(?:[1-9](?:[0-9])*|0)'
#     pattern = rf'(?:{num}(?:[+*]{num})*)'
#     prog = sorted(re.findall(pattern, s), reverse=True, key=len)
#     ans = [x for x in prog]
#     c = 0
#     test = r'[+][1-9]+[+]'
#     mx = 0
#     for x in ans:
#         if c == 20:
#             break
#         match = re.search(test, x)
#         tmp = []
#         print(x,len(x), match)
#         c+=1
#     print(mx)
# #
# #9753
# with open("24_9753.txt") as f:
#     s = f.read()
#     r = l =0
#     c = 0
#     while l < len(s) and r < len(s):
#         if s[l:r].count("Y") <150:
#             r+= 1
#         else :
#             c = max(len(s[l:r]),c)
#             l+= 1
#     print(c)
#9753
# with open("24.5_19717.txt") as f:
#     s = f.read()
#     r = l =0
#     c = 0
#     while l < len(s)  and r < len(s):
#         if s[l:r].count("M") <279:
#             r+= 1
#         else :
#             c = max(len(s[l:r]),c)
#             if c ==2472:
#                 break
#             l+= 1
#     print(c)
# def f(s):
#     if len(s) == 1:
#         return 1

import re

ans = 0
def task(ex):
    tmp = []
    for i in range(len(ex)):
        if ex[i] in '-*':
            continue
        elif ex[i] == '0' and i != len(ex)- 1 and ex[i+1] in '0123456789':
            continue
        else:
            for j in range(len(ex) - 1, i, -1):
                if ex[j] in '-*':
                    continue
                if ex[i:j].count('-') + ex[i:j].count('*') != 0:
                    tmp.append(ex[i:j + 1])
    return tmp

with open("24_19884.txt") as f:
    s = f.read()
    num = r'(?:[6-9](?:[06789])*|0)'
    pattern = rf'(?:{num}(?:[-*]{num})+)'

    for exp in re.findall(pattern, s):
        ans += len(task(exp))

    print(ans)