def task(n):
    ans = ''
    while n>0:
        last = n % 4
        n = n // 4
        ans = str(last) + ans
    return ans
mx = 0
otv = 0
for x in range(1,3001):
    if task(4**210+4**110-x).count('0') > mx:
        mx =  task(4**210+4**110-x).count('0')
        otv = x
print(mx, otv)