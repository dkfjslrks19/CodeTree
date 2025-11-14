arr = list(map(int, input().split()))

big = arr[0]

if arr[1] > big:
    big = arr[1]

if arr[2] > big:
    big = arr[2]

print(big)