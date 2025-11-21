arr = []
sum, cnt = 0, 0

for _ in range(10):
    arr.append(int(input()))

for i in range(10):
    if arr[i]>=0 and arr[i]<=200:
        sum += arr[i]
        cnt += 1
avg = f'{sum/cnt:.1f}'

print(sum, avg)
