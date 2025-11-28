n = int(input())

# 위쪽(가운데 포함)
for i in range(1, n+1):
    print(' ' * (n-i) + '*' * (2*i-1))

# 아래쪽
for i in range(n-1, 0, -1):
    print(' ' * (n-i) + '*' * (2*i-1))