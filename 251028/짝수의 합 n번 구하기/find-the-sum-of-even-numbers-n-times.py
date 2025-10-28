n = int(input())

for _ in range(n):
    a, b = map(int, input().split())
    if a > b:
        a, b = b, a  # (혹시 모를 역순 입력 대비)

    start = a if a % 2 == 0 else a + 1
    end   = b if b % 2 == 0 else b - 1

    if start > end:
        print(0)
        continue

    k = ((end - start) // 2) + 1
    s = k * (start + end) // 2
    print(s)