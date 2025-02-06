def f(a, b, m):
    if a+ b>=59: return m % 2 == 0 # условие победы
    if m == 0: return 0 # условие оканчания
    h = [f(a + 1,b, m - 1), f(a * 2,b, m - 1), f(a,b+1,  m - 1), f(a,b*2,  m - 1)]
    if m%2!= 0:
        return  any(h)
    else:
        return all(h) # Если был совершен неудачный ход, то all -> any

# Устанавливаем стартовые позиции, если надо делаем две кучи
print('19)', [s for s in range(1, 54) if f( 5,s, 2)])
print('20)', [s for s in range(1, 2199) if f(s, 3) and not f(s, 1) ])
print('21)', [s for s in range(1, 2199) if  f( s, 4)])