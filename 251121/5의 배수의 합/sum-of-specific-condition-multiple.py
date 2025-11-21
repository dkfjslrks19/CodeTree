a, b = map(int, input().split())

small = min(a, b)
big = max(a, b)

sum = 0

for i in range(small, big+1):
    if i % 5 == 0:
        sum += i

print(sum)