def f (x,y,A):
    return (x+3*y> A )or (x< 18) or (y<33)
for a in range(1000):
    if all(f(x,y,a) for x in range(1,1001) for y in range(1,1001)):
        print(a)