a = list(map(int,input().split()))

if a[0] >= a[1]:
    if a[2]>=a[0]:
        print(a[0])
    elif a[1]>=a[2]:
        print(a[1])
    else:
        print(a[2])
else: #a[0]<=a[1]
    if a[1]<=a[2]:
        print(a[1])
    elif a[0]<=a[2]:
        print(a[2])
    else:
        print(a[0])