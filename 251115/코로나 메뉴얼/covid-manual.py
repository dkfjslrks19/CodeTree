a = list(input().split())
b = list(input().split())
c = list(input().split())

num = 0


if a[0]=='Y' and int(a[1])>=37:
    num += 1
if b[0]=='Y' and int(b[1])>=37:
    num += 1
if c[0]=='Y' and int(c[1])>=37:
    num += 1
if num>=2:
    print('E')
else:
    print('N')    