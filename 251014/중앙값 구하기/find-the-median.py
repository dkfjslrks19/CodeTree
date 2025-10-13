a,b,c = map(int,input().split())

if a<b:
    if b<c:
        print(b)
    else:
        print(c)
elif b<c:
    if c<a:
        print(c)
    else:
        print(a)
else:
    if a<b:
        print(a)
    else:
        print(b)