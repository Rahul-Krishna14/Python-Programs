def cap(x):
    l = ''
    for i in x:
        if i == ' ':
            l = l + ' '
        elif ord(i) >= 95 and ord(i) <= 122:
            a = ord(i) - 32
            l = l + chr(a)
    print(l)

cap(input())