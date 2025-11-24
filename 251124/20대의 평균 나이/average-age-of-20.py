total = 0
cnt = 0

while True:
    age = int(input())
    if not (20 <= age <= 29):   # 20대가 아니면 즉시 종료
        break
    total += age
    cnt += 1

print(f"{total/cnt:.2f}")