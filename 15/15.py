# def f (x,y,A):
#     return (x+3*y> A )or (x< 18) or (y<33)
# for a in range(1000):
#     if all(f(x,y,a) for x in range(1,1001) for y in range(1,1001)):
#         print(a)
#
# def f(x, a1, a2):
#     P = 117 <= x <= 158
#     Q = 130 <= x <= 180
#     A = a1 <= x <= a2
#     return P <= ((not A and Q)  <= (not P))
# ans = []
# for a2 in range(1, 1000):
#     for a1 in range(1, 1000):
#         if all(f(x,a1,a2) for x in range(1,500)) and a2 > a1:
#             ans.append(a2-a1)
# print(min(ans))

def task(a1,a2,x):
    B = 36<=x<=75
    C = 60<=x<=110
    A = a1 <= x <= a2
    return (not A) <= ((B) == C)
ans = []
for a1 in range(1,200):
    for a2 in range(a1,200):
        if all(task(a1,a2,x) for x in range(1,1000)):
            ans.append(a2-a1)
print(min(ans))
