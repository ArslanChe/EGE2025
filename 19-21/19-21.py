def f(a,  m):
    if a>=128: return m % 2 == 0 # условие победы
    if m == 0: return 0 # условие оканчания
    h = [f(a + 2, m - 1), f(a +5, m - 1),f(a *2, m - 1), ]
    if m%2!= 0:
        return  any(h)
    else:
        return all(h) # Если был совершен неудачный ход, то all -> any

# Устанавливаем стартовые позиции, если надо делаем две кучи
print('19)', [s for s in range(1, 127) if not f( s, 1) and  f( s, 2)])
print('19)', [s for s in range(1, 127) if not f( s, 1) and  f( s, 3)])
print('19)', [s for s in range(1, 127) if not f( s, 2) and  f( s, 4)])