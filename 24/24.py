# with open("24_318.txt") as f:
#     s = f.read()
#     for i in range(len(s)):
#         if s[i].isalpha():
#             s = s.replace(s[i], ' ')
#     print(s.split())
from re import *
from fnmatch import fnmatch
# with open("24_18285.txt") as f:
#     s = f.read()
#     num = r'(?:[1-9](?:[0-9])*)'
#     pattern = rf'(?:{num}(?:[+*]{num})*)'
#     prog = findall(pattern, s)
#     ans = max([ len(list(x.replace('*', '+').split('+'))) for x in prog])
#     print(ans)


#9753
with open("24_9753.txt") as f:
    s = f.read()
    r = l =0
    c = 0
    while l < len(s) and r < len(s):
        if s[l:r].count("Y") <150:
            r+= 1
        else :
            c = max(len(s[l:r]),c)
            l+= 1
    print(c)