with open("24_318.txt") as f:
    s = f.read()
    for i in range(len(s)):
        if s[i].isalpha():
            s = s.replace(s[i], ' ')
    print(s.split())