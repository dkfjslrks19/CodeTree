n = int(input())
sum, cnt = 0, 0

for _ in range(n):
    a = int(input())
    sum += a
    cnt += 1
avg = f'{sum/cnt:.1f}'
print(sum,avg)