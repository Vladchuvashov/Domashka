a = 0
b = 0
c = 0
d = int(input())
while d != 0:
    if a == d:
        b += 1
    else:
        a = d
        c = max(c, b)
        b = 1
    d = int(input())
c = max(c, b)
print(c)