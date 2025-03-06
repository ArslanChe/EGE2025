# with open("24_318.txt") as f:
#     s = f.read()
#     for i in range(len(s)):
#         if s[i].isalpha():
#             s = s.replace(s[i], ' ')
#     print(s.split())
import re
mx = 0
with open("24_17641.txt") as f:
    s = f.read()
    num = r'(?:[1-9](?:[0-9])*|0)'
    pattern = rf'(?:{num}(?:[+*]{num})*)'
    prog = sorted(re.findall(pattern, s), reverse=True, key=len)
    ans = [x for x in prog]
    c = 0
    test = r'[+][1-9]+[+]'
    mx = 0
    for x in ans:
        if c == 20:
            break
        match = re.search(test, x)
        tmp = []
        print(x,len(x), match)
        c+=1
    print(mx)
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