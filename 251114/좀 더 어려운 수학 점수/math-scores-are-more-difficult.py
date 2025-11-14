a = list(map(int,input().split()))
b = list(map(int,input().split()))

if a[0]>b[0] or (a[0]==b[0] and a[1]>b[1]):
    print('A')
else:
    print('B')
