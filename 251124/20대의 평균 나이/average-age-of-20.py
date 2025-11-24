total = 0
cnt = 0

while True:
    age = int(input())
    if age >= 30:
        break
    total += age
    cnt += 1

if cnt == 0:
    print("0.00")  # 문제에 맞는 출력 형식으로 변경 가능
else:
    print(f'{total/cnt:.2f}')