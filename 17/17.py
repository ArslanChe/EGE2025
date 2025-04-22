def check(a):
    return  1000 <= abs(a) <= 9999 and abs(a) % 10 == 6
c = 0
sm = 0
with open('17_21712.txt') as f:
    l = list(map(int,f.readlines()))
    mnc6 = [x for x in sorted(l) if 1000 <= x <= 9999 and x % 10 == 6][0]
    for troi in zip(l,l[1:],l[2:]):
        if sum(troi)<= mnc6 and check(troi[0]) + check(troi[1])+ check(troi[2]) == 1:
            c+=1
            sm = max(sm, sum(troi))
print(sm, c)