n = int(input())

# 각 열의 별 개수 계산
stars = []
for j in range(1, n+1):
    if j % 2 == 1:   # 홀수 열
        stars.append(1)
    else:            # 짝수 열
        stars.append(j)
                                        
# i는 행 (1~n)
for i in range(1, n+1):
    for j in range(n):  # 열
        if stars[j] >= i:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()