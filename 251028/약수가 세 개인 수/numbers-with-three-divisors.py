start, end = map(int, input().split())

# Please write your code here.
cnt = 0  # 약수가 3개인 수의 개수

for i in range(start, end + 1):   # start부터 end까지
    count = 0                     # i의 약수 개수
    for a in range(1, i + 1):     # 1부터 i까지 나눠보기
        if i % a == 0:
            count += 1
    if count == 3:                # 약수가 3개면
        cnt += 1

print(cnt)