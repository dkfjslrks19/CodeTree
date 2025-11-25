a,b = map(int,input().split())


if (1920 % a==0 and 2880%a==0) or (1920%b==0 and 2880%b==0):
    print(1)
else:
    print(0)
