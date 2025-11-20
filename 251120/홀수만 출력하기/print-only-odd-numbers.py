n = int(input())
arr = []

for _ in range(n):
    arr.append(int(input()))

for x in arr:
    if x % 3 == 0 and x % 2 == 1:
        print(x)