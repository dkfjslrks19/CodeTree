n = int(input())

for i in range(1, n + 1):        # i: 1 ~ n (행)
    for j in range(1, n + 1):    # j: 1 ~ n (열)
        if i == 1 or i == n:     # 첫 줄, 마지막 줄은 전체 별
            print('*', end=' ')
        else:
            if j <= i - 1 or j == n:   # 왼쪽 삼각형 + 오른쪽 테두리
                print('*', end=' ')
            else:
                print(' ', end=' ')
    print()